#!/usr/bin/env python3
"""Check repository-local Markdown links and heading anchors without networking."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


def prose(text: str) -> str:
    lines = []
    fence: tuple[str, int] | None = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = (token[0], len(token))
            elif (fence[0] == token[0] and len(token) >= fence[1]
                  and not line[marker.end():].strip()):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines)


def anchors(path: Path) -> set[str]:
    found = set()
    counts: dict[str, int] = {}
    text = prose(path.read_text(encoding="utf-8"))
    for heading in re.findall(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", text, re.MULTILINE):
        heading = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", heading)
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        number = counts.get(slug, 0)
        candidate = slug if number == 0 else f"{slug}-{number}"
        while candidate in found:
            number += 1
            candidate = f"{slug}-{number}"
        counts[slug] = number + 1
        found.add(candidate)
    found.update(re.findall(r'\b(?:id|name)=["\x27]([^"\x27]+)["\x27]', text))
    return found


def check(root: Path) -> tuple[int, list[str]]:
    count = 0
    errors = []
    for source in sorted(root.rglob("*.md")):
        if any(part in {".git", ".venv", "node_modules"} for part in source.relative_to(root).parts):
            continue
        text = prose(source.read_text(encoding="utf-8"))
        targets = re.findall(r"\]\(\s*(<[^>]+>|[^\s)]+)", text)
        targets += re.findall(r"^\s{0,3}\[[^]]+\]:\s*(<[^>]+>|\S+)", text, re.MULTILINE)
        for raw in targets:
            target = raw.strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            count += 1
            path = (source.parent / unquote(parsed.path)).resolve() if parsed.path else source
            label = f"{source.relative_to(root)}: {target}"
            if not path.exists():
                errors.append(f"{label}: missing target")
            elif parsed.fragment and path.suffix.lower() == ".md" and unquote(parsed.fragment) not in anchors(path):
                errors.append(f"{label}: missing anchor")
    return count, errors


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    root = Path(args[0]).resolve() if args else Path(__file__).resolve().parents[1]
    count, errors = check(root)
    for error in errors:
        print(error)
    print(f"{count} local links checked; {len(errors)} problems")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
