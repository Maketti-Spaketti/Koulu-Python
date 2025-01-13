########################################################
# Task A10_T5
# Developer Markus Kivinen
# Date 2024-11-22
########################################################
import sys


def get_int(prompt: str) -> int:
    value = input(prompt)
    return int(value)


def recursiveFactorial(PNum: int) -> int:
    if PNum == 1:
        return PNum
    return recursiveFactorial(PNum - 1) * PNum


def main() -> None:
    print("Program starting.")
    if len(sys.argv) > 1:
        value = int(sys.argv[1])
    else:
        value = get_int("Insert factorial: ")
    print(f"Factorial {value}!")
    fac = recursiveFactorial(value)
    fac_string = "*".join([str(i) for i in range(1, value + 1)])
    print(f"{fac_string} = {fac}")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
