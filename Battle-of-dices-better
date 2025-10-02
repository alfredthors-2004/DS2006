# Battle of Dices is going to be an amazing 2 player game,
# where two players face each other using only their sheer luck!
#
# The rules are:
#
# Each player throws one D6.
# The player with the highest roll wins the round.
# The first player to win 3 times is the winner.
#
# Our main task today is to implement the code necessary to bring this
# amazing game alive!

import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
round_number = 1

# Play the game until someone wins 3 times
while player1_wins < 3 and player2_wins < 3:
    input(f"\nRound {round_number}: Press ENTER to roll the dice...")

    player1_roll = random.randint(1, 6)
    player2_roll = random.randint(1, 6)

    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    if player1_roll > player2_roll:
        player1_wins += 1
        print(" Player 1 wins this round!")

    elif player2_roll > player1_roll:
        player2_wins += 1
        print("Player 2 wins this round!")

# Show current score

print(f"Score: Player 1 = {player1_wins} | Player 2 = {player2_wins}")
round_number += 1

# Announce the overall winner
if player1_wins == 3:
    print("\nPlayer 1 is the newest Battle of Dices Champion!!")
else:
    print("\nPlayer 2 is the newest Battle of Dices Champion!!")