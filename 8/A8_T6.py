########################################################
# Task A8_T6
# Developer Markus Kivinen
# Date 2024-11-09
########################################################
from A8_T1Lib import Input, Canvas
from pathlib import Path

MENUOPTIONS: dict[int, str] = {
    1: "Draw square",
    2: "Draw circle",
    3: "Save svg",
    0: "Exit",
}
ROOT_PATH = Path(__file__).parent


def main() -> None:
    print("Program starting.")
    canvas = Canvas.Canvas()
    while True:
        Input.showOptions("Options:", MENUOPTIONS)
        choice = Input.getIntInput("Your choice: ")
        if choice == -1:
            print("Unknown option!\n")
            continue
        elif choice == 0:
            print("Exiting program.\n")
            break

        elif choice == 1:
            print("Insert square")
            x = Input.getFloatInput("- Left edge position: ")
            y = Input.getFloatInput("- Top edge position: ")
            w = Input.getFloatInput("- Side length: ")
            fill = Input.getStrInput("- Fill color: ")
            stroke = Input.getStrInput("- Stroke color: ")
            print("")
            canvas.addRect(x, y, w, w, fill, stroke)
        elif choice == 2:
            print("Insert circle")
            x = Input.getFloatInput("- Center X coord: ")
            y = Input.getFloatInput("- Center Y coord: ")
            r = Input.getFloatInput("- Radius: ")
            fill = Input.getStrInput("- Fill color: ")
            stroke = Input.getStrInput("- Stroke color: ")
            canvas.addCircle(x, y, r, fill, stroke)
            print("")
        elif choice == 3:
            filename = Input.getStrInput("Insert filename: ")
            print(f'Saving file to "{filename}"')
            if Input.getConfirmation("Proceed (y/n)?: "):
                filepath = ROOT_PATH / filename
                if filepath.suffix != ".svg":
                    filename += ".svg"
                canvas.setname(str(filepath))
                canvas.save()
                print("Vector saved successfully!\n")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
