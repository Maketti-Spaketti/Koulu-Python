########################################################
# Task A9_T1

# Developer Markus Kivinen
# Date 2024-11-15
########################################################


def collectNumbers() -> float:
    summed = 0.0
    while True:
        try:
            user_input = input("Insert a floating-point value (0 to stop): ")
            if user_input == "0":
                return summed
            summed += float(user_input)
        except ValueError:
            print(f"Error! '{user_input}' couldn't be converted to float.")


def main() -> None:
    print("Program starting.\n")
    summed = collectNumbers()
    print("\nFinal sum is {:.2f}".format(summed))
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
