########################################################
# Task A10_T1
# Developer Markus Kivinen
# Date 2024-11-22
########################################################
from pathlib import Path
import sys

ROOT_FOLDER = Path(__file__).parent


def get_filename(prompt: str) -> str:
    filename = input(prompt)
    return filename


def read_file(filename: str, values: list[str]) -> None:
    filepath = ROOT_FOLDER / filename
    values.extend(x for x in filepath.read_text().splitlines() if x)


def print_values(results: list):
    print("# --- Vertically --- #")
    print("\n".join(results))
    print("# --- Vertically --- #")
    print("# --- Horizontally --- #")
    print(", ".join(results))
    print("# --- Horizontally --- #")


def main() -> None:
    print("Program starting.")
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = get_filename("Insert filename: ")
    values: list[str] = []
    read_file(filename, values)
    print_values(values)
    values.clear()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
