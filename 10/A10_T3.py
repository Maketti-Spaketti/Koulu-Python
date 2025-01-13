########################################################
# Task A10_T3
# Developer Markus Kivinen
# Date 2024-11-22
########################################################
import sys


def get_filename(prompt: str) -> str:
    filename = input(prompt)
    return filename


def read_values(filename: str, PValues: list[int]) -> None:
    with open(filename, "r", encoding="utf-8") as file:
        PValues.extend(int(x) for x in file.read().splitlines() if x)


def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    length = len(PValues)
    for i in range(length):
        is_sorted = True
        for x in range(0, length - i - 1):
            if (PAsc and PValues[x] > PValues[x + 1]) or (
                not PAsc and PValues[x] < PValues[x + 1]
            ):
                PValues[x], PValues[x + 1] = PValues[x + 1], PValues[x]
                is_sorted = False
        # exit out if no swaps were made
        if is_sorted:
            return None


def print_results(prompt: str, sorted_values: list[int]) -> None:
    print(f"# --- {prompt} --- #")
    print(", ".join(map(str, sorted_values)))
    print(f"# --- {prompt} --- #")


def main() -> None:
    print("Program starting.")
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        print(f"The filename '{filename}' was passed via CLI.")
    else:
        filename = get_filename("Insert filename: ")
    values: list[int] = []
    read_values(filename, values)

    print(f"Raw '{filename}' -> " + ", ".join(map(str, values)))
    bubbleSort(values, True)
    print(f"Ascending '{filename}' -> " + ", ".join(map(str, values)))
    bubbleSort(values, False)
    print(f"Descending '{filename}' -> " + ", ".join(map(str, values)))

    values.clear()
    return None


if __name__ == "__main__":
    main()
