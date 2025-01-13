########################################################
# User/Credentials library
# Developer Markus Kivinen
# Date 2024-11-08
########################################################
from dataclasses import dataclass


# Order by ID, biggest ID = newest user
@dataclass(order=True)
class User:
    id: int
    username: str
    hashed_password: str

    def passwordMatches(self, password: str) -> bool:
        """Checks if the password matches the user's password.
        Args:
            password (str): The password to check.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        import hashlib

        return (
            self.hashed_password == hashlib.md5(password.encode()).hexdigest()
        )

    def setPassword(self, password: str) -> None:
        """Sets the user's password.
        Args:
            password (str): The unhashed password to set.
        """
        self.hashed_password = User.hashPassword(password)

    @classmethod
    def frominput(
        cls, username: str, password: str, users: dict[str, "User"]
    ) -> "User":
        """Creates a new user from input.
        Args:
            username (str): The username.
            password (str): The unhashed password.
            users (dict[str, User]): The existing users.

        Returns:
            User: The new user.
        """
        return cls(
            User.getNextFreeUserId(users),
            username,
            User.hashPassword(password),
        )

    @staticmethod
    def hashPassword(password: str) -> str:
        """Hashes the password.
        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        import hashlib

        return hashlib.md5(password.encode()).hexdigest()

    @staticmethod
    def getNextFreeUserId(users: dict[str, "User"]) -> int:
        """Returns the next free user id.
        Args:
            users (dict[str, User]): The users.

        Returns:
            int: The next free user id.
        """
        return max([user.id for user in users.values()], default=-1) + 1

    def serialize(self) -> str:
        """Serializes the user.
        format: id;username;password
        """
        return f"{self.id};{self.username};{self.hashed_password}"


class Credentials:
    @staticmethod
    def readCredentials(filename: str) -> dict[str, "User"]:
        """Reads credentials from a file and returns them as a dictionary.
        Args:
            filename (str): The name of the file.

        Returns:
            dict[str, User]: username -> User
        """
        try:
            with open(filename, "r") as file:
                users = {}
                for line in file.read().splitlines():
                    id, username, password = line.split(";")
                    users[username] = User(int(id), username, password)
                return users
        except FileNotFoundError:
            return {}

    @staticmethod
    def saveCredentials(filename: str, users: dict[str, "User"]) -> None:
        """Saves credentials to a file.
        Args:
            filename (str): The name of the file.
            users (dict[str, User]): The credentials to save.
        """
        with open(filename, "w") as file:
            file.write("\n".join(user.serialize() for user in users.values()))
