def collectNumbers(numbers: list[int]) -> None:
    user_input = input("Insert comma separated integers: ")
    for i in user_input.split(","):
        # .isdecimal, isdigit, ja isnumeric eivät toimi nega/deci
        try:
            numbers.append(int(i))
        except ValueError:
            print(f"Invalid value '{i}' detected.")
    return None


def displayNumbers(numbers: list[int]) -> None:
    if len(numbers) == 0:
        print("No values to analyse.")
        return None
    print(f"There are {len(numbers)} integers in the list.")
    summed = sum(numbers)
    odd_even = "even" if summed % 2 == 0 else "odd"
    print(f"Sum of the integers is {summed} and it's {odd_even}")
    return None


def main() -> None:
    print("Program starting.")
    numbers: list[int] = []
    collectNumbers(numbers)
    displayNumbers(numbers)
    numbers.clear()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
