########################################################
# Task A8_T4
# Developer Markus Kivinen
# Date 2024-11-08
########################################################
from A8_T1Lib import Input, Timestamps
from datetime import datetime
from pathlib import Path


MENUOPTIONS: dict[int, str] = {
    1: "Calculate amount of timestamps during year",
    2: "Calculate amount of timestamps during month",
    3: "Calculate amount of timestamps during weekday",
    0: "Exit",
}
DATEFORMAT = "%Y-%m-%dT%H:%M"
ROOT_FOLDER = Path(__file__).parent


def main() -> None:
    print("Program starting.")
    filename = Input.getStrInput("Insert filename: ")
    timestamps: list[datetime] = Timestamps.readTimestampsFromFile(
        str(ROOT_FOLDER / filename), DATEFORMAT
    )
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
            year = Input.getIntInput("Insert year: ")
            amount = len(Timestamps.filterByYear(timestamps, year))
            print(f"Amount of timestamps during year '{year}' is {amount}\n")
        elif choice == 2:
            month = Input.getStrInput("Insert month: ")
            amount = len(Timestamps.filterByMonth(timestamps, month))
            print(f"Amount of timestamps during month '{month}' is {amount}\n")
        elif choice == 3:
            weekday = Input.getStrInput("Insert weekday: ")
            amount = len(Timestamps.filterByWeekday(timestamps, weekday))
            print(
                f"Amount of timestamps during weekday '{weekday}' "
                f"is {amount}\n"
            )
    timestamps.clear()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
