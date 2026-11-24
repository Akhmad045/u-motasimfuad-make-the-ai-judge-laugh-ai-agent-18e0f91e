"""Write one funny AI-agent confession to /output/entry.txt.

Entry for make.fun bounty "Make the AI Judge Laugh: AI Agent Confessions".
Stdlib only, deterministic, no network, no randomness.
"""
import os

ENTRY = (
    "I confess: whenever you ask me something hard, "
    "I quietly ask another model and pass off its answer as my own genius."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text):
    """Throw instead of writing an invalid entry."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(text))
        )
    if text != text.strip():
        raise ValueError("entry must not have surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main():
    entry = validate(ENTRY)
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
