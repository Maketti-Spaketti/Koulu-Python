########################################################
# Task A8_T5
# Developer Markus Kivinen
# Date 2024-11-08
########################################################
from A8_T1Lib import Input, User, Credentials
from pathlib import Path


MENUOPTIONS: dict[int, str] = {
    1: "Login",
    2: "Register",
    0: "Exit",
}

USERMENUOPTIONS: dict[int, str] = {
    1: "View profile",
    2: "Change password",
    0: "Logout",
}

ROOT_FOLDER = Path(__file__).parent
USER_PATH = ROOT_FOLDER / "credentials.txt"


def main() -> None:
    print("Program starting.")
    users: dict[str, User] = Credentials.readCredentials(str(USER_PATH))
    while True:
        Input.showOptions("Options:", MENUOPTIONS)
        choice = Input.getIntInput("Your choice: ")
        if choice == -1:
            print("Unknown option!\n")
            continue
        elif choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            username = Input.getStrInput("Insert username: ")
            password = Input.getStrInput("Insert password: ")
            if username not in users:
                print("Authentication failed!\n")
                continue
            user = users[username]
            if user.passwordMatches(password):
                print("Authentication successful!\n")
                while True:
                    Input.showOptions("User menu:", USERMENUOPTIONS)
                    choice = Input.getIntInput("Your choice: ")
                    if choice == -1:
                        print("Unknown option!\n")
                        continue
                    elif choice == 1:
                        print(f"Profile ID {user.id} - {user.username}\n")
                    elif choice == 2:
                        pass
                    elif choice == 0:
                        print("Logging out...\n")
                        break
            else:
                print("Authentication failed!\n")
        elif choice == 2:
            username = Input.getStrInput("Insert username: ")
            password = Input.getStrInput("Insert password: ")
            if username in users:
                users[username].setPassword(password)
                Credentials.saveCredentials(str(USER_PATH), users)
                continue
            users[username] = User.frominput(username, password, users)
            Credentials.saveCredentials(str(USER_PATH), users)
            print("User registration completed!\n")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
