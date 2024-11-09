def showOptions() -> None:
    options: dict[int, str] = {
        1: "Show count",
        2: "Increase count",
        3: "Reset count",
        0: "Exit",
    }
    print("Options:")
    for i in options:
        print(i, "-", options[i])
    return None


def askChoice() -> int:
    try:
        return int(input("Your choice: "))
    except ValueError:
        return -1


def main() -> None:
    count: int = 0
    print("Program starting.")
    while True:
        showOptions()
        match (askChoice()):
            case 1:
                print(f"Current count - {count}\n")
            case 2:
                count += 1
                print("Count increased!\n")
            case 3:
                count = 0
                print("Cleared count!\n")
            case 0:
                print("Exiting program.\n")
                break
            case _:
                print("Unknown option!\n")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
