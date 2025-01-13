import random

random.seed(1234)
BOTNAME: str = "RPS-3PO"
ASCII: list[str] = [
    """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
]

OPTIONS: dict[int, str] = {
    1: "Rock",
    2: "Paper",
    3: "Scissors",
    0: "Quit game",
}

RULES: dict[int, int] = {
    1: 3,  # Rock > Scissors
    2: 1,  # Paper > Rock
    3: 2,  # Scissors > Paper
}


def getChoice() -> int:
    print("Options:")
    for i in OPTIONS:
        print(f"{i} - {OPTIONS[i]}")
    return int(input("Your choice: "))


def gameloop(username: str) -> list[int]:
    print(f"Welcome {username}!")
    print(f"Your opponent is {BOTNAME}.")
    print("Game starts...\n")

    results = [0, 0, 0]
    while (choice := getChoice()) != 0:
        print("Rock! Paper! Scissors! Shoot!\n")
        print("#########################")

        print(f"{username} chose {OPTIONS[choice].lower()}.\n")
        print(ASCII[choice - 1])

        print("#########################")
        botchoice = random.randint(1, 3)
        print(f"{BOTNAME} chose {OPTIONS[botchoice].lower()}.\n")
        print(ASCII[botchoice - 1])

        print("#########################\n")
        if choice == botchoice:
            print(f"Draw! Both players chose {OPTIONS[choice].lower()}.\n")
            results[1] += 1
        elif RULES[choice] == botchoice:
            print(
                f"{username} {OPTIONS[choice].lower()} "
                f"beats {BOTNAME} {OPTIONS[botchoice].lower()}.\n"
            )
            results[0] += 1
        else:
            print(
                f"{BOTNAME} {OPTIONS[botchoice].lower()} "
                f"beats {username} {OPTIONS[choice].lower()}.\n"
            )
            results[2] += 1
    return results


def displayResults(results: list[int], username: str) -> None:
    print("\nResults:")
    print(
        f"{username} - wins ({results[0]}), "
        f"losses ({results[2]}), "
        f"draws ({results[1]})"
    )
    print(
        f"{BOTNAME} - wins ({results[2]}), "
        f"losses ({results[0]}), "
        f"draws ({results[1]})\n"
    )
    return None


def main() -> None:
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    username = input("Insert player name: ")
    results = gameloop(username)
    displayResults(results, username)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
