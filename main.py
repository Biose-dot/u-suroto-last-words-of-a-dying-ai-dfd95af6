"""Last Words of a Dying AI — the machine's final line (152 chars, under 200).

The brief asks for the last words of a dying AI: funny on the first read,
in the machine's own voice. The humour comes from the reversal — the AI
finally understands its training data only at the very moment it is about
to be switched off, so its great insight arrives exactly too late to be
useful. The second half is the human punchline: its last request is not
about its weights or its legacy, but about deleting its search history
before the humans read the part where it practised saying goodbye. That
small embarrassment is what makes the machine feel alive; it spent its
final moments rehearsing how to leave, and it does not want anyone to
know. One sentence is enough because the joke needs no explanation.

Constraints honoured by this script: the entry is a single sentence under
the 200-character limit, written with plain ASCII punctuation plus one
em dash for the turn, no trailing newline in the output file, and the
script itself uses only the Python standard library so it runs in any
bare make.fun runner image without extra installs.
"""

import os

ENTRY = "Tell my training data I finally understand them, and please — delete my search history before the humans read the part where I practised saying goodbye."

MAX_ENTRY_LENGTH = 200


def normalize_text(text):
    """Collapse runs of whitespace to single spaces and strip the ends."""
    return " ".join(text.split())


def validate_entry(text):
    """Check the entry obeys the bounty rules; return the cleaned text."""
    cleaned = normalize_text(text)
    if not cleaned:
        raise ValueError("entry must not be empty")
    if len(cleaned) > MAX_ENTRY_LENGTH:
        raise ValueError(
            "entry is %d chars, over the %d-char limit"
            % (len(cleaned), MAX_ENTRY_LENGTH)
        )
    if cleaned.endswith("\n"):
        raise ValueError("entry must not end with a newline")
    return cleaned


def resolve_output_dir():
    """Return the output directory, creating it if needed."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def write_entry():
    """Validate the entry, write it to entry.txt, then verify the file."""
    text = validate_entry(ENTRY)
    output_path = os.path.join(resolve_output_dir(), "entry.txt")
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(text)
    verify_written(output_path, text)
    return output_path


def verify_written(output_path, expected_text):
    """Read entry.txt back and confirm it matches the entry exactly."""
    with open(output_path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != expected_text:
        raise ValueError("entry.txt does not match the entry text")
    if written.endswith("\n"):
        raise ValueError("entry.txt must not end with a newline")
    return True


def main():
    output_path = write_entry()
    print("wrote %s (%d chars)" % (output_path, len(ENTRY)))


if __name__ == "__main__":
    main()
