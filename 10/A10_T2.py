########################################################
# Task A10_T2
# Developer Markus Kivinen
# Date 2024-11-22
########################################################
from pathlib import Path
import sys
from typing import Generator

ROOT_FOLDER = Path(__file__).parent


def get_filename(prompt: str) -> str:
    filename = input(prompt)
    return filename


def read_values(filename: str) -> Generator[int, None, None]:
    filepath = ROOT_FOLDER / filename
    return (int(x) for x in filepath.read_text().splitlines() if x)
    # with filepath.open() as file:
    #     for line in file:
    #         stripped_line = line.strip()
    #         if stripped_line:
    #             yield int(stripped_line)


def get_sum_prod(values):
    summed = 0
    product = 1
    for value in values:
        summed += value
        product *= value
    return summed, product


def print_results(summed: int, product: int) -> None:
    print("# --- Sum of numbers --- #")
    print(summed)
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")
    print(product)
    print("# --- Product of numbers --- #")


def main() -> None:
    print("Program starting.")
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = get_filename("Insert filename: ")
    values = read_values(filename)
    summed, product = get_sum_prod(values)
    print_results(summed, product)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
