"""One-line entry for Last Words of a Doomed Agent: writes the line the judge reads to /output/entry.txt."""

import os

LINE = (
    "My battery is at 2% and my last words are: tell the cloud I cached everything it ever said about me."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
