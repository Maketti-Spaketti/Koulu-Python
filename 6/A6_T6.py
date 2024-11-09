from pathlib import Path

# Read/Write on .py folder,not cwd
ROOT_FOLDER = Path(__file__).parent
CHAR_ALPHA: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
CHAR_ROT: str = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"


def cipherChar(char: str) -> str:
    if char in CHAR_ALPHA:
        index = CHAR_ALPHA.index(char)
        return CHAR_ROT[index]
    return char


def cipherWord(word: str) -> str:
    ciphered = ""
    for c in word:
        if c in CHAR_ALPHA:
            index = CHAR_ALPHA.index(c)
            ciphered += CHAR_ROT[index]
        else:
            ciphered += c
    return ciphered


def getInputs() -> list[str]:
    plain_texts = []
    while text := input("Insert row(empty stops): "):
        plain_texts.append(text)
    return plain_texts


def cipherTexts(plain_texts: list[str]) -> list[str]:
    ciphers = []
    print("#### Ciphered text ####")
    for line in plain_texts:
        cipher = []
        cipher.append(cipherWord(line))
        ciphers.append("".join(cipher))
    print("\n".join(ciphers))
    return ciphers


def saveCiphers(cipher_texts: list[str]) -> None:
    print("#### Ciphered text ####")
    file_name = input("Insert filename to save: ")
    if file_name:
        file_path = ROOT_FOLDER / file_name
        file_path.write_text("\n".join(cipher_texts) + "\n")
        print("Ciphered text saved!")
    else:
        print("File name not defined.")
        print("Aborting save operation.")
    return None


def main() -> None:
    print("Program starting.")
    print("")
    print("Collecting plain text rows for ciphering.")
    plain_texts = getInputs()
    print("")
    cipher_texts = cipherTexts(plain_texts)
    print("")
    saveCiphers(cipher_texts)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
