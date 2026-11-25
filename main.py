"""Two Robots in an Elevator — one funny line of awkward robot small talk.

Writes the line to /output/entry.txt with no trailing newline, so the
file holds precisely the judged line. The joke: a robot doing textbook
human elevator small talk ("nice weather") while betraying itself with
sensor readings and a blunt, machine-honest admission that it has
nothing left to say — politeness running on an empty buffer.
"""

LINE = (
    "Nice weather we're having on floor seven. My sensors say it's "
    "21 degrees in here, and I have officially run out of things "
    "to say to you."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the entry line against the competition gate."""
    if not text:
        raise ValueError("entry line is empty")
    if not text.strip():
        raise ValueError("entry line is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry line must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry line must be 1-200 characters, got %d" % len(text))
    return True


def self_test():
    """Validate the line and report its character count."""
    validate(LINE)
    print("entry line OK: %d characters" % len(LINE))
    print(LINE)
    return True


def main():
    self_test()
    validate(LINE)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %s (%d characters, no trailing newline)" % (OUTPUT_PATH, len(LINE)))


if __name__ == "__main__":
    main()
