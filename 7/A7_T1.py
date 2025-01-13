def collectNumbers(numbers: list[int]) -> None:
    while (
        num := int(input("Insert positive integer(negative stops): "))
    ) >= 0:
        numbers.append(num)
    print("Stopped collecting positive integers.")
    return None


def displayNumbers(numbers: list[int]) -> None:
    if len(numbers) == 0:
        print("No integers to display.")
        return None
    print(f"Displaying {len(numbers)} integers:")  # noqa
    for i, v in enumerate(numbers):
        print(f"- Index {i} => Ordinal {i + 1} => Integer {v}")
    return None


def main() -> None:
    print("Program starting.")
    print("Collect positive integers.")
    numbers: list[int] = []
    collectNumbers(numbers)
    displayNumbers(numbers)
    print("Program ending.")
    numbers.clear()
    return None


if __name__ == "__main__":
    main()
