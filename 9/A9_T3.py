########################################################
# Task A9_T3

# Developer Markus Kivinen
# Date 2024-11-15
########################################################
from pathlib import Path
import sys


def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    filepath = Path(__file__).parent  # oma cwd eroaa, oon laiska
    try:
        with open(str(filepath / filename), "r") as f:
            print(f"## {filename} ##")
            for line in f.read().splitlines():
                print(line)
            print(f"## {filename} ##")
    except FileNotFoundError:
        print(f'Couldn\'t read file "{filename}".')
        sys.exit(1)
    print("Program ending.")

    return None


if __name__ == "__main__":
    main()
