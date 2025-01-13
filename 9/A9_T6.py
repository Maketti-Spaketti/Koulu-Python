########################################################
# Task A9_T6

# Developer Markus Kivinen
# Date 2024-11-18
########################################################
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent

MENUOPTIONS: dict[str, str] = {
    "1": "- Insert line",
    "2": "- Save lines",
    "0": "- Exit",
}


def printOptions() -> None:
    print("Options:")
    for key, value in MENUOPTIONS.items():
        print(f"{key} {value}")
    return None


def getLine() -> str:
    return input("Insert text: ")


def saveLines(lines: list[str]) -> None:
    filename = input("Insert filename: ")
    with open(ROOT_FOLDER / filename, "w") as file:
        for line in lines:
            file.write(line + "\n")
    return None


def main() -> None:
    lines: list[str] = []
    print("Program starting.")
    while True:
        try:
            printOptions()
            menu_choice = input("Your choice: ")
            match menu_choice:
                case "1":
                    lines.append(getLine())
                    print("")
                case "2":
                    saveLines(lines)
                case "0":
                    break
                case _:
                    print("Unknown option!\n")
        except KeyboardInterrupt:
            if lines:
                print("Keyboard interrupt and unsaved progress!")
                save = input("Save before quit(y/n)?: ")
                if save == "y":
                    saveLines(lines)
                break
            else:
                print("Closing suddenly.")
                break
    lines.clear()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
