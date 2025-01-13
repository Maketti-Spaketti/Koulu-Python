########################################################
# Task A10_T6
# Developer Markus Kivinen
# Date 2024-11-22
########################################################
import time
from pathlib import Path
from typing import Callable
from copy import deepcopy

ROOT_FOLDER = Path(__file__).parent


def get_filename(prompt: str) -> str:
    filename = input(prompt)
    return filename


def read_values(filename: str, PValues: list[int]) -> None:
    filepath = ROOT_FOLDER / filename
    PValues.extend(int(x) for x in filepath.read_text().splitlines() if x)


def BubbleSort(PNums: list[int]) -> list[int]:
    length = len(PNums)
    for i in range(length):
        Sorted = True
        for j in range(length - i - 1):
            if PNums[j] > PNums[j + 1]:
                PNums[j], PNums[j + 1] = PNums[j + 1], PNums[j]
                Sorted = False
        if Sorted:
            break
    return PNums


def quickSort(PValues: list[int]) -> list[int]:
    # Median of three is slower for small datasets
    if len(PValues) <= 1:
        return PValues
    pivot = PValues[0]
    less = [x for x in PValues[1:] if x <= pivot]
    greater = [x for x in PValues[1:] if x > pivot]
    return quickSort(less) + [pivot] + quickSort(greater)


def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    StartTime = time.perf_counter_ns()
    PSortingAlgorithm(PArr)
    EndTime = time.perf_counter_ns()
    ElapsedTime = EndTime - StartTime
    return ElapsedTime


def printOptions() -> None:
    print("Options:")
    print("1 - Read dataset values")
    print("2 - Measure speeds")
    print("3 - Save results")
    print("0 - Exit")
    return None


def main() -> None:
    print("Program starting.")

    Values: list[int] = []
    Results: list[str] = []

    while True:
        printOptions()
        choice = input("Your choice: ")
        if choice == "0":
            print("Exiting program.\n")
            break
        elif choice == "1":
            filename = input("Insert dataset filename: ")
            read_values(filename, Values)
            Results.append(f"Measured speeds for dataset '{filename}':")
            print("")
        elif choice == "2":
            sorted_time = measureSortingTime(sorted, deepcopy(Values))
            bubble_time = measureSortingTime(BubbleSort, deepcopy(Values))
            quick_time = measureSortingTime(quickSort, deepcopy(Values))
            Results.append(f" - Built-in sorted {sorted_time} ns")
            Results.append(f" - Buble sort {bubble_time} ns")
            Results.append(f" - Quick sort {quick_time} ns")
            print("\n".join(Results))
            print("")
        elif choice == "3":
            filename = input("Insert results filename: ")
            with open(filename, "w") as file:
                for result in Results:
                    file.write(result + "\n")
            print("")
    Values.clear()
    Results.clear()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
