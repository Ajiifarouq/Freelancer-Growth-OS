from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

TEXT_SUFFIXES = {".md", ".py", ".toml", ".yml", ".yaml", ".json", ".txt"}
DENIED_DIR_PARTS = {
    ".fgos",
    "fgos-data",
    "local-data",
    "private-data",
    "user-data",
    "runtime-data",
    "data",
    "exports",
    "backups",
    "logs",
    "artifacts",
    "imports",
    "uploads",
    "eval-results",
    ".eval-results",
}
DENIED_SUFFIXES = {
    ".db",
    ".sqlite",
    ".sqlite3",
    ".db-wal",
    ".db-shm",
    ".sqlite-wal",
    ".sqlite-shm",
    ".pem",
    ".p12",
    ".pfx",
    ".key",
}

SECRET_PATTERNS = {
    "OpenAI-style API key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "GitHub classic token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "GitHub fine-grained token": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "private key block": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}

MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def tracked_files() -> list[Path]:
    proc = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [ROOT / item.decode() for item in proc.stdout.split(b"\0") if item]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_path_safety(path: Path, errors: list[str]) -> None:
    rel = path.relative_to(ROOT)
    parts = set(rel.parts[:-1])
    name = rel.name

    if name == ".env" or (name.startswith(".env.") and name != ".env.example"):
        fail(errors, f"forbidden tracked environment file: {rel}")

    if parts & DENIED_DIR_PARTS:
        fail(errors, f"forbidden tracked runtime/private-data path: {rel}")

    if any(str(rel).endswith(suffix) for suffix in DENIED_SUFFIXES):
        fail(errors, f"forbidden tracked secret/database artifact: {rel}")


def read_text_if_applicable(path: Path) -> str | None:
    if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {".gitignore", ".editorconfig", "CODEOWNERS"}:
        return None
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def check_text_hygiene(path: Path, text: str, errors: list[str]) -> None:
    rel = path.relative_to(ROOT)
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        fail(errors, f"text file does not end with newline: {rel}")

    for label, pattern in SECRET_PATTERNS.items():
        if pattern.search(text):
            fail(errors, f"possible {label} committed in {rel}")

    if path.suffix.lower() == ".md":
        h1_count = sum(1 for line in text.splitlines() if re.match(r"^#\s+\S", line))
        if h1_count != 1:
            fail(errors, f"Markdown file must contain exactly one H1 ({h1_count} found): {rel}")
        check_markdown_links(path, text, errors)


def check_markdown_links(path: Path, text: str, errors: list[str]) -> None:
    rel = path.relative_to(ROOT)
    for match in MARKDOWN_LINK.finditer(text):
        target = match.group(1).strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0].split("?", 1)[0]
        if not target:
            continue
        target_path = (path.parent / target).resolve()
        try:
            target_path.relative_to(ROOT.resolve())
        except ValueError:
            fail(errors, f"Markdown link escapes repository in {rel}: {target}")
            continue
        if not target_path.exists():
            fail(errors, f"broken repository-local Markdown link in {rel}: {target}")


def main() -> int:
    errors: list[str] = []
    for path in tracked_files():
        if not path.exists() or not path.is_file():
            continue
        check_path_safety(path, errors)
        text = read_text_if_applicable(path)
        if text is not None:
            check_text_hygiene(path, text, errors)

    if errors:
        print("Repository governance checks FAILED:\n", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Repository governance checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
