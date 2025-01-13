########################################################
# Task A10_T4
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


def merge(
    PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool
) -> None:
    result = []
    while PLeft and PRight:
        if (PAsc and PLeft[0] <= PRight[0]) or (
            not PAsc and PLeft[0] >= PRight[0]
        ):
            result.append(PLeft.pop(0))
        else:
            result.append(PRight.pop(0))

    result.extend(PLeft or PRight)
    PMerge[:] = result


def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    if len(PValues) <= 1:
        return

    middle = len(PValues) // 2
    left = PValues[:middle]
    right = PValues[middle:]

    mergeSort(left, PAsc)
    mergeSort(right, PAsc)
    merged: list[int] = []
    merge(left, right, merged, PAsc)

    PValues[:] = merged


def main() -> None:
    print("Program starting.")
    values: list[int] = []
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        print(f"The filename '{filename}' was passed via CLI.")
    else:
        filename = get_filename("Insert filename: ")
    read_values(filename, values)
    print(f"Raw '{filename}' -> " + ", ".join(map(str, values)))
    mergeSort(values, True)
    print(values)
    # print(f"Ascending '{filename}' -> " + ", ".join(map(str, values)))
    # mergeSort(values, False)
    # print(f"Descending '{filename}' -> " + ", ".join(map(str, values)))
    values.clear()
    return None


if __name__ == "__main__":
    main()
