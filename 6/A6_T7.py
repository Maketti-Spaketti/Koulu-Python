from pathlib import Path

# Read/Write on .py folder,not cwd
ROOT_FOLDER = Path(__file__).parent
SAVE_PATH = ROOT_FOLDER / "player_progress.txt"
# SAVE_PATH.unlink()
HEADER = "current_location;next_location;passphrase"
CHAR_ALPHA: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
CHAR_ROT: str = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
LOCATIONS: dict[str, str] = {
    "0": "home",
    "1": "Galba's palace",
    "2": "Otho's palace",
    "3": "Vitellius' palace",
    "4": "Vespasian's palace",
}


def decipherString(Strings: str) -> str:
    Output = []
    for c in Strings:
        if c in CHAR_ALPHA:
            index = CHAR_ALPHA.index(c)
            Output.append(CHAR_ROT[index])
        else:
            Output.append(c)
    return "".join(Output)


def decipherMessages(Messages: list[str]) -> list[str]:
    Output = []
    for i in Messages:
        Output.append(decipherString(i))
    return Output


def saveGame(GameState, Announce=True) -> None:
    if Announce:
        print("[Game] Progress autosaved!")
    SAVE_PATH.write_text("\n".join(GameState))
    return None


def loadGame() -> list[str]:
    GameState = []
    if not SAVE_PATH.exists():
        GameState = [HEADER, "0;1;qvfpvcyvar\n"]
        saveGame(GameState, Announce=False)
    else:
        GameState = SAVE_PATH.read_text().splitlines()
    while GameState[-1] == "":
        GameState.pop()
    return GameState


def saveMessage(Location: str, Passphrase: str, Message: str) -> None:
    # OutPath = ROOT_FOLDER / f"{Location}-{Passphrase}.txt"
    # OutPath.write_text(Message + "\n")
    with open(f"{Location}-{Passphrase}.txt", "w") as f:
        f.write(Message + "\n")
    return None


def progressGame(GameState: list[str]) -> None:
    _, NextLocation, Passphrase = GameState[-1].split(";")
    print("Looking for the message in the palace...")
    FilePath = ROOT_FOLDER / f"{NextLocation}_{Passphrase}.gkg"
    FileContent = FilePath.read_text().splitlines()
    print("Ah, there it is! Seems cryptic.")

    # PreviousLocation, NextLocation, Passphrase = FileContent[0].split(";")
    GameState.append(FileContent[0])
    saveGame(GameState)

    # Read emperors message
    Messages = FileContent[1:]

    # Decipher passphrase
    # _ = decipherString(passphrase)
    # Decipher emperors message
    PlainMessage = "\n".join(decipherMessages(Messages))

    print(
        "Deciphering Emperor's message...\n"
        "Looks like I've got now the plain "
        "version copy of the Emperor's message.\n"
        "Time to leave..."
    )
    saveMessage(NextLocation, decipherString(Passphrase), PlainMessage)
    return None


def printCurrentLocation(LocKey: str) -> None:
    print(f"Currently at {LOCATIONS[LocKey]}.")
    return None


def travelTo(Loc: str) -> None:
    print(f"Travelling to {LOCATIONS[Loc]}...")
    print(f"...Arriving to the {LOCATIONS[Loc]}.")
    print("Passing the guard at the entrance.")
    return None


def tellPassphrase(CipheredPass: str) -> None:
    DecipheredPass = decipherString(CipheredPass)
    print(f'"{DecipheredPass.capitalize()}!"')
    return None


def main() -> None:
    print("Travel starting.")
    GameState = loadGame()
    CurrentLocation, NextLocation, CipheredPass = GameState[-1].split(";")
    printCurrentLocation(CurrentLocation)
    travelTo(NextLocation)
    tellPassphrase(CipheredPass)
    progressGame(GameState)
    print("Travel ending.")
    return None


if __name__ == "__main__":
    main()
