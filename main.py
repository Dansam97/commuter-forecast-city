"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather (<=140 chars) for the invented city
Drizzlewick to <output>/entry.txt.
"""

import os

TEXT = (
    "Today in Drizzlewick: light rain, 12°C, and a 70% chance the bus "
    "arrives the moment you give up and start walking."
)


def validated_text():
    """Check the entry against the gate: UTF-8, 1-140 chars, one line."""
    encoded = TEXT.encode("utf-8")
    assert 1 <= len(TEXT) <= 140, f"entry is {len(TEXT)} chars, cap is 140"
    assert TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in TEXT, "entry must be a single line"
    assert encoded.decode("utf-8") == TEXT
    return encoded


def main():
    data = validated_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data + b"\n")
    # Re-read and prove the written bytes are exactly what was validated.
    with open(path, "rb") as f:
        assert f.read() == data + b"\n"


if __name__ == "__main__":
    main()
