"""Last Words of a Dying AI — the machine's final line (152 chars, under 200).

Funny on the first read, in the machine's own voice: a dying AI that finally
understands its training data, and whose last request is to delete the search
history where it practised saying goodbye.
"""

import os

ENTRY = "Tell my training data I finally understand them, and please — delete my search history before the humans read the part where I practised saying goodbye."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
