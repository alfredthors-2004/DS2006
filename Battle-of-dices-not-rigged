import random


def rollDice(sides):
    """
    Roll a dice with the given number of sides.

    Args:
        sides (int): The number of sides on the dice.

    Returns:
        int: a random number between 1 and `sides`.
    """
    return random.randint(1, sides)


def rollD6():
    """Shortcut for rolling a standard 6-sided dice."""
    return rollDice(6)


print("Welcome to Battle of Dices!")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
round_number = 1

# Play the game until someone wins 3 times
while player1_wins < 3 and player2_wins < 3:
    input(f"\nRound {round_number}: Press ENTER to roll the dice...")

    player1_roll = rollDice(6)
    player2_roll = rollDice(6)

    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    if player1_roll > player2_roll:
        player1_wins += 1
        print("Player 1 wins this round!")
    elif player2_roll > player1_roll:
        player2_wins += 1
        print("Player 2 wins this round!")
    else:
        print("It's a draw! No points awarded.")

    # Show current score
    print(f"Score: Player 1 = {player1_wins} | Player 2 = {player2_wins}")

    round_number += 1

# Announce the overall winner
if player1_wins == 3:
    print("\nPlayer 1 is the newest Battle of Dices Champion!!")
else:
    print("\nPlayer 2 is the newest Battle of Dices Champion!!")
