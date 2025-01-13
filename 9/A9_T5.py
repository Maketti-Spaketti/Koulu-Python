########################################################
# Task A9_T5

# Developer Markus Kivinen
# Date 2024-11-15
########################################################
from dataclasses import dataclass


@dataclass
class Color:
    red: int = 0
    green: int = 0
    blue: int = 0

    @property
    def hexadecimal(self) -> str:
        return "#{:02x}{:02x}{:02x}".format(self.red, self.green, self.blue)


def createRGB() -> Color | None:
    color = Color()
    inputs = ["red", "green", "blue"]
    for c in inputs:
        try:
            value = input(f"Insert {c}: ")
            int_value = int(value)
            if 0 <= int_value <= 255:
                setattr(color, c, int_value)
            else:
                print(f'Value "{value}" is out of the range 0-255.')
                return None
        except ValueError:
            print(f'"{value}" is non-numeric value.')
            return None
    return color


def main() -> None:
    print("Program starting.")
    color = createRGB()
    if color:
        print("RGB Details:")
        print("- Red", color.red)
        print("- Green", color.green)
        print("- Blue", color.blue)
        print("- Hex", color.hexadecimal)
    else:
        print(
            "Couldn't perform the designed task "
            "due to the invalid input values."
        )
    print("Program ending.")

    return None


if __name__ == "__main__":
    main()
