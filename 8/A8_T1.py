########################################################
# Task A8_T1
# Developer Markus Kivinen
# Date 2024-11-08
########################################################
from A8_T1Lib import Input, Utility

MENUOPTIONS: dict[int, str] = {
    1: "Set pause duration",
    2: "Activate pause",
    0: "Exit",
}


def main() -> None:
    print("Program starting.")
    duration: float = 0
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
            temp = Input.getFloatInput("Insert pause duration (s): ")
            if temp == -1:
                print("Unknown option!\n")
                continue
            duration += temp
            print("")
        elif choice == 2:
            if duration == 0:
                print("Pause is not set.\nSet pause first.\n")
                continue
            print(f"Pausing for {round(duration, 2)} seconds.")
            Utility.sleep(duration)
            print("Unpaused.\n")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
