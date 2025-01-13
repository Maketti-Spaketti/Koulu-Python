########################################################
# Task A9_T4

# Developer Markus Kivinen
# Date 2024-11-15
########################################################


def collectCelcius() -> float:
    value = input("Insert Celsius: ")
    try:
        float_value = float(value)
        if -273.15 <= float_value <= 10000:
            return float_value
        print(f"{float_value:.1f} temperature out of range.")
        return -1
    except ValueError:
        print(f"could not convert string to float: '{value}'")
        return -1


def main() -> None:
    print("Program starting.")
    value = collectCelcius()
    if value != -1:
        print("You inserted {:.1f} °C".format(value))
    print("Program ending.")

    return None


if __name__ == "__main__":
    main()
