########################################################
# Task A9_T7

# Developer Markus Kivinen
# Date 2024-11-18
########################################################
import sys
import os


def getInput(prompt: str) -> str:
    return input(prompt)


def copy_file(src: str, dst: str) -> None:
    with open(src, "r") as src_file, open(dst, "w") as dst_file:
        for line in src_file:
            dst_file.write(line)


def main() -> None:
    print("Program starting.")

    try:
        src, dst = sys.argv[1:]
        print(f'Source file "{src}"')
        print(f'Destination file "{dst}"')
        print(f'Copying file "{src}" to "{dst}".')

        if not os.path.exists(src):
            print(f'Couldn\'t copy "{src}" to "{dst}".')
            print("Exiting program.")
            sys.exit(1)
        elif os.path.exists(dst):
            print(f'Destination file "{dst}" already exists.')
            overwrite = input("Do you want to overwrite it? (y/n): ")
            if overwrite == "y":
                copy_file(src, dst)
        else:
            copy_file(src, dst)
    except ValueError:
        print("Invalid amount of arguments.")
        print("[USAGE] python A9_T7.py src_file dst_file")

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
