########################################################
# Task A8_T3
# Developer Markus Kivinen
# Date 2024-11-08
########################################################
from A8_T1Lib import Input, Utility
from pathlib import Path


MENUOPTIONS: dict[int, str] = {
    1: "Read values",
    2: "Amount of values",
    3: "Calculate sum of values",
    4: "Calculate average of values",
    0: "Exit",
}
ROOT_FOLDER = Path(__file__).parent


def main() -> None:
    print("Program starting.")
    values: list[float] = []
    while True:
        Input.showOptions("Options:", MENUOPTIONS)
        choice = Input.getIntInput("Your choice: ")
        if choice == -1:
            print("Unknown option!\n")
            continue
        elif choice == 0:
            print("Exiting program.\n")
            break

        if choice == 1:
            filename = Input.getStrInput("Insert filename: ")
            values = Utility.readFloatsFromFile(str(ROOT_FOLDER / filename))
            print("")
        elif choice == 2:
            print(f"Amount of values {len(values)}\n")
        elif choice == 3:
            print(f"Sum of values {sum(values):.1f}\n")
        elif choice == 4:
            print(f"Average of values {sum(values) / len(values):.1f}\n")
    values.clear()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
