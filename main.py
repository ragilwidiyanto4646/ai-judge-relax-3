import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

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
