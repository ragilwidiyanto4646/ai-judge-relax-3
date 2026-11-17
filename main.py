"""Write the lakeshore-at-dawn entry for the ai-judge-relax-01 bounty.

The program writes a single slow, sensory text: a still lake before
sunrise, mist lifting a little at a time, rings spreading across the
water and fading. The text is fixed in this module, so the output is
deterministic and byte-identical on every run.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The entry text is fixed; it is written out as UTF-8 bytes.
TEXT = "\n".join([
    "Before sunrise the lake lay grey and still.",
    "A thin mist rested on the water.",
    "Far out, a fish rose, and one small ring spread across the surface.",
    "The ring widened, slowly, until it reached the reeds.",
    "The sky lightened above the far shore.",
    "A pale line of sun touched the water.",
    "The mist thinned and lifted, a little at a time.",
    "A second ring appeared, then faded.",
    "The reeds stood dark against the light.",
    "The water held the sky.",
    "The rings were gone.",
    "The lake was quiet.",
])


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "wb") as f:
        f.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
