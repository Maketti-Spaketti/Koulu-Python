########################################################
# Task A8_T2
# Developer Markus Kivinen
# Date 2024-11-08
########################################################
from A8_T1Lib import Input, Math

MENUOPTIONS: dict[int, str] = {
    1: "Add",
    2: "Subtract",
    3: "Multiply",
    4: "Divide",
    0: "Exit",
}


def main() -> None:
    print("Program starting.")
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
            first = Input.getFloatInput("Insert first addend value: ")
            second = Input.getFloatInput("Insert second addend value: ")
            added = Math.add(first, second)
            print(f"{first:.1f} + {second:.1f} = {added:.1f}\n")
        if choice == 2:
            first = Input.getFloatInput("Insert minuend value: ")
            second = Input.getFloatInput("Insert subtrahend value: ")
            subbed = Math.substract(first, second)
            print(f"{first:.1f} - {second:.1f} = {subbed:.1f}\n")
        if choice == 3:
            first = Input.getFloatInput("Insert multiplicand value: ")
            second = Input.getFloatInput("Insert multiplier value: ")
            multiplied = Math.multiply(first, second)
            print(f"{first:.1f} * {second:.1f} = {multiplied:.1f}\n")
        if choice == 4:
            first = Input.getFloatInput("Insert dividend value: ")
            second = Input.getFloatInput("Insert divisor value: ")
            divided = Math.divide(first, second)
            print(f"{first:.1f} / {second:.1f} = {divided:.1f}\n")

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
