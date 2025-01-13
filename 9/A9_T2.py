########################################################
# Task A9_T2

# Developer Markus Kivinen
# Date 2024-11-15
########################################################
import sys


def main() -> None:
    print("Program starting.")
    exit_code = int(input("Insert exit code(0-255): "))
    if exit_code == 0:
        print("Clean exit")
    else:
        print("Error code")
    sys.exit(exit_code)
    return None


if __name__ == "__main__":
    main()
