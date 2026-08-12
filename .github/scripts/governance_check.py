from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

TEXT_SUFFIXES = {".md", ".py", ".toml", ".yml", ".yaml", ".json", ".txt"}
EXPLICIT_TEXT_NAMES = {
    ".gitignore",
    ".editorconfig",
    ".env.example",
    "CODEOWNERS",
}
DENIED_TOP_LEVEL_DIRS = {
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
    "tmp",
    "temp",
    "eval-results",
    ".eval-results",
    "test-output",
}
DENIED_SUFFIXES = {
    ".db",
    ".sqlite",
    ".sqlite3",
    ".db-wal",
    ".db-shm",
    ".db-journal",
    ".sqlite-wal",
    ".sqlite-shm",
    ".sqlite-journal",
    ".sqlite3-wal",
    ".sqlite3-shm",
    ".sqlite3-journal",
    ".pem",
    ".p12",
    ".pfx",
    ".key",
    ".jks",
    ".keystore",
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
    name = rel.name

    if name == ".env" or (name.startswith(".env.") and name != ".env.example"):
        fail(errors, f"forbidden tracked environment file: {rel}")

    # Runtime/private-data names are reserved only at repository root. This avoids
    # accidentally forbidding legitimate source packages such as src/.../data/.
    if rel.parts and rel.parts[0] in DENIED_TOP_LEVEL_DIRS:
        fail(errors, f"forbidden tracked repository-root runtime/private-data path: {rel}")

    if any(str(rel).endswith(suffix) for suffix in DENIED_SUFFIXES):
        fail(errors, f"forbidden tracked secret/database artifact: {rel}")


def check_secret_patterns(path: Path, raw: bytes, errors: list[str]) -> None:
    # Scan every tracked file, regardless of extension. latin-1 preserves every
    # byte one-to-one while still exposing ASCII token/private-key markers that
    # may be embedded in oddly named configuration files or binary containers.
    rel = path.relative_to(ROOT)
    scan_text = raw.decode("latin-1")
    for label, pattern in SECRET_PATTERNS.items():
        if pattern.search(scan_text):
            fail(errors, f"possible {label} committed in {rel}")


def read_text_if_applicable(path: Path, raw: bytes) -> str | None:
    if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in EXPLICIT_TEXT_NAMES:
        return None
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return None


def check_text_hygiene(path: Path, raw: bytes, text: str, errors: list[str]) -> None:
    rel = path.relative_to(ROOT)
    if raw and not raw.endswith(b"\n"):
        fail(errors, f"text file does not end with newline: {rel}")

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


def run_self_tests() -> int:
    failures: list[str] = []

    def expect_error(label: str, action) -> None:
        errors: list[str] = []
        action(errors)
        if not errors:
            failures.append(f"self-test expected failure but passed: {label}")

    def expect_clean(label: str, action) -> None:
        errors: list[str] = []
        action(errors)
        if errors:
            failures.append(f"self-test expected clean result but failed: {label}: {errors}")

    fake_openai_key = b"sk" + b"-" + (b"a" * 32)
    expect_error(
        ".env.example secret scan",
        lambda errors: check_secret_patterns(
            ROOT / ".env.example",
            b"OPENAI_API_KEY=" + fake_openai_key + b"\n",
            errors,
        ),
    )
    expect_clean(
        ".env.example placeholder",
        lambda errors: check_secret_patterns(
            ROOT / ".env.example",
            b"OPENAI_API_KEY=\n",
            errors,
        ),
    )
    expect_error(
        "SQLite rollback journal denied",
        lambda errors: check_path_safety(ROOT / "fixture.sqlite-journal", errors),
    )
    expect_error(
        "SQLite3 rollback journal denied",
        lambda errors: check_path_safety(ROOT / "fixture.sqlite3-journal", errors),
    )
    expect_error(
        "Java keystore denied",
        lambda errors: check_path_safety(ROOT / "fixture.jks", errors),
    )
    expect_error(
        "generic keystore denied",
        lambda errors: check_path_safety(ROOT / "fixture.keystore", errors),
    )
    expect_error(
        "repository-root runtime data denied",
        lambda errors: check_path_safety(ROOT / "runtime-data" / "fixture.txt", errors),
    )
    expect_clean(
        "nested source data directory allowed",
        lambda errors: check_path_safety(ROOT / "src" / "freelancer_growth_os" / "data" / "models.py", errors),
    )

    if failures:
        print("Governance self-tests FAILED:\n", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("Governance self-tests passed.")
    return 0


def main() -> int:
    errors: list[str] = []
    for path in tracked_files():
        if not path.exists() or not path.is_file():
            continue
        check_path_safety(path, errors)
        raw = path.read_bytes()
        check_secret_patterns(path, raw, errors)
        text = read_text_if_applicable(path, raw)
        if text is not None:
            check_text_hygiene(path, raw, text, errors)

    if errors:
        print("Repository governance checks FAILED:\n", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Repository governance checks passed.")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        raise SystemExit(run_self_tests())
    raise SystemExit(main())
