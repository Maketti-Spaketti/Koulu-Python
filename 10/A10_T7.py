########################################################
# Task A10_T7
# Developer Markus Kivinen
# Date 2024-11-28
########################################################
import random

random.seed(1234)


def layMines(PMineField: list[list[int]], PMines: int):
    rows = len(PMineField)
    columns = len(PMineField[0])
    while PMines > 0:
        row = random.randint(0, rows - 1)
        column = random.randint(0, columns - 1)
        if PMineField[row][column] != 9:
            PMineField[row][column] = 9
            PMines -= 1
    return None


def calculateNearbys(PMineField: list[list[int]]) -> None:
    pairs: list[list[int]] = [
        [-1, 0],
        [1, 0],
        [0, 1],
        [0, -1],
        [-1, -1],
        [-1, 1],
        [1, -1],
        [1, 1],
    ]
    rows = len(PMineField)
    columns = len(PMineField[0])
    for row in range(rows):
        for column in range(columns):
            if PMineField[row][column] == 9:
                for x, y in pairs:
                    r, c = row + x, column + y
                    if (
                        0 <= r < rows
                        and 0 <= c < columns
                        and PMineField[r][c] != 9
                    ):
                        PMineField[r][c] += 1
    return None


def generateMinefield(
    PMineField: list[list[int]], PRows: int, PCols: int, PMines: int
) -> None:
    PMineField[:] = [[0 for _ in range(PCols)] for _ in range(PRows)]
    layMines(PMineField, PMines)
    calculateNearbys(PMineField)
    return None


def printOptions() -> None:
    print("Options:")
    print("1 - Generate minesweeper board")
    print("2 - Show generated board")
    print("3 - Save generated board")
    print("0 - Exit")


def main() -> None:
    print("Program starting.")
    PMineField: list[list[int]] = []
    while True:
        printOptions()
        choice = input("Your choice: ")
        if choice == "0":
            print("Exiting program.\n")
            break
        elif choice == "1":
            rows = int(input("Insert rows: "))
            columns = int(input("Insert columns: "))
            mines = int(input("Insert mines: "))
            generateMinefield(PMineField, rows, columns, mines)
            print("")
        elif choice == "2":
            for row in PMineField:
                print(f"[{", ".join(map(str, row))}]")
        elif choice == "3":
            filename = input("Insert filename: ")
            with open(filename, "w") as file:
                for row in PMineField:
                    file.write(",".join(map(str, row)) + "\n")
            print("")
    PMineField.clear()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
