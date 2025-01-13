from pathlib import Path
from dataclasses import dataclass
from typing import Self


ORD_A: int = ord("A")


@dataclass
class Rotor:
    _values: str
    _pos: int
    _length: int = 0

    def __post_init__(self):
        self._length = len(self._values)

    def forward_index(self, index) -> int:
        index = (
            self._values.index(
                chr(((index + self._pos) % self._length) + ORD_A)
            )
            - self._pos
            + self._length
        ) % self._length
        return index

    def backward_index(self, index) -> int:
        offset = (self._pos + index) % self._length
        index = (
            ord(self._values[offset]) - ORD_A - self._pos + self._length
        ) % self._length
        return index

    def rotate(self):
        self._pos = (self._pos + 1) % self._length


class Enigma:
    def __init__(self, rotor1: str, rotor2: str, rotor3: str, reflector: str):
        """Only supports 3 rotors"""
        self._rotor1 = Rotor(rotor1, 0)
        self._rotor2 = Rotor(rotor2, 0)
        self._rotor3 = Rotor(rotor3, 0)
        self._reflector = reflector

    @classmethod
    def from_file(cls, filepath: str) -> Self:
        with open(filepath, encoding="utf-8") as f:
            data = f.read()
        lines = data.splitlines()
        rotor1 = lines[0][7:]
        rotor2 = lines[1][7:]
        rotor3 = lines[2][7:]
        reflector = lines[3][10:]
        enigma = cls(rotor1, rotor2, rotor3, reflector)
        return enigma

    def reset_positions(self):
        self._rotor1._pos = 0
        self._rotor2._pos = 0
        self._rotor3._pos = 0

    def rotate(self):
        self._rotor1.rotate()
        if self._rotor1._pos == 0:
            self._rotor2.rotate()
            if self._rotor2._pos == 0:
                self._rotor3.rotate()

    def scramble(self, word: str) -> str:
        ciphered = ""

        for char in word.upper():
            # A-Z
            if not char.isalpha():
                ciphered += char
                continue

            self.rotate()

            index = ord(char) - ORD_A
            index = self._rotor1.forward_index(index)
            index = self._rotor2.forward_index(index)
            index = self._rotor3.forward_index(index)

            char = self._reflector[index]
            index = ord(char) - ORD_A

            index = self._rotor3.backward_index(index)
            index = self._rotor2.backward_index(index)
            index = self._rotor1.backward_index(index)
            char = chr(index + ORD_A)

            ciphered += char
        return ciphered


def main() -> None:
    filename = input("Insert config(filename): ") or "iconf1.txt"
    plugs = input("Insert plugs (y/n)?: ") or "n"
    if plugs == "n":
        print("No extra plugs inserted.")
    ROOT_FOLDER = Path(__file__).parent
    filepath = ROOT_FOLDER / filename
    enigma = Enigma.from_file(str(filepath))
    print("Enigma initialized.\n")
    while word := input("Insert row (empty stops): "):
        scrambled = enigma.scramble(word)
        for i, i2 in zip(word, scrambled):
            print(f'Character "{i}" illuminated as "{i2}"')
        print(f'Converted row - "{scrambled}".\n')
        enigma.reset_positions()
    print("\nEnigma closing.")
    return None


if __name__ == "__main__":
    main()
