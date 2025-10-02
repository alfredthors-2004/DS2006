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

import sys

print("Welcome to Battle of Dices!")

input(f"\nPress ENTER to start the game...")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
round_number = 1

# Definition of a 6-sided dice


def rollD6():
    """
    Roll a standard 6-sided dice.

    Returns:
        int: a random number between 1 and 6
         """
    return random.randint(1, 6)


def check_for_winner():
    if player1_wins == 3 or player2_wins == 3:
        print("\nGame Over!")
        print("\nMatch Summary:")
        for r, p1, p2 in list_of_rounds:
            print(f"Round {r}: Player 1 rolled {p1} player 2 rolled {p2}")
        if player1_wins == 3:
            print("\nPlayer 1 is the winner!")
        elif player2_wins == 3:
            print("\nPlayer 2 is the winner!")
        else:
            print("Nobody reached 3 points!! What a shame!!")
        sys.exit()

# List to store the history of each rounds


list_of_rounds = []

# Round 1
input("\nPress ENTER to roll the dice for Player 1...")
player1_round1_roll = rollD6()
print("Player 1 rolled:", player1_round1_roll)
input("\nPress ENTER to roll the dice for Player 2...")
player2_round1_roll = rollD6()
print("Player 2 rolled:", player2_round1_roll)

list_of_rounds.append((round_number, player1_round1_roll, player2_round1_roll))

if player1_round1_roll > player2_round1_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
elif player1_round1_roll == player2_round1_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")

# Round 2

round_number += 1
input("\nPress ENTER to roll the dice for Player 1...")
player1_round2_roll = rollD6()
print("Player 1 rolled:", player1_round2_roll)
input("\nPress ENTER to roll the dice for Player 2...")
player2_round2_roll = rollD6()
print("Player 2 rolled:", player2_round2_roll)

list_of_rounds.append((round_number, player1_round2_roll, player2_round2_roll))

if player1_round2_roll > player2_round2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
elif player1_round2_roll == player2_round2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")

# Round 3

round_number += 1
input("\nPress ENTER to roll the dice for Player 1...")
player1_round3_roll = rollD6()
print("Player 1 rolled:", player1_round3_roll)
input("\nPress ENTER to roll the dice for Player 2...")
player2_round3_roll = rollD6()
print("Player 2 rolled:", player2_round3_roll)

list_of_rounds.append((round_number, player1_round3_roll, player2_round3_roll))

if player1_round3_roll > player2_round3_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
elif player1_round3_roll == player2_round3_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
check_for_winner()

# Round 4

round_number += 1
input("\nPress ENTER to roll the dice for Player 1...")
player1_round4_roll = rollD6()
print("Player 1 rolled:", player1_round4_roll)
input("\nPress ENTER to roll the dice for Player 2...")
player2_round4_roll = rollD6()
print("Player 2 rolled:", player2_round4_roll)

list_of_rounds.append((round_number, player1_round4_roll, player2_round4_roll))

if player1_round4_roll > player2_round4_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
elif player1_round4_roll == player2_round4_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
check_for_winner()

# Round 5

round_number += 1
input("\nPress ENTER to roll the dice for Player 1...")
player1_round5_roll = rollD6()
print("Player 1 rolled:", player1_round5_roll)
input("\nPress ENTER to roll the dice for Player 2...")
player2_round5_roll = rollD6()
print("Player 2 rolled:", player2_round5_roll)

list_of_rounds.append((round_number, player1_round5_roll, player2_round5_roll))

if player1_round5_roll > player2_round5_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
elif player1_round5_roll == player2_round5_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
check_for_winner()

# Round 6

round_number += 1
input("\nPress ENTER to roll the dice for Player 1...")
player1_round6_roll = rollD6()
print("Player 1 rolled:", player1_round6_roll)
input("\nPress ENTER to roll the dice for Player 2...")
player2_round6_roll = rollD6()
print("Player 2 rolled:", player2_round6_roll)

list_of_rounds.append((round_number, player1_round6_roll, player2_round6_roll))

if player1_round6_roll > player2_round6_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
elif player1_round6_roll == player2_round6_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
check_for_winner()

# Round 7

round_number += 1
input("\nPress ENTER to roll the dice for Player 1...")
player1_round7_roll = rollD6()
print("Player 1 rolled:", player1_round7_roll)
input("\nPress ENTER to roll the dice for Player 2...")
player2_round7_roll = rollD6()
print("Player 2 rolled:", player2_round7_roll)

list_of_rounds.append((round_number, player1_round7_roll, player2_round7_roll))

if player1_round7_roll > player2_round7_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
elif player1_round7_roll == player2_round7_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
check_for_winner()

# Game over

print("\nGame Over!")

# Print round-by-round history"
print("\nMatch Summary:")
for r, p1, p2 in list_of_rounds:
    print(f"Round {r}: Player 1 rolled {p1} player 2 rolled {p2}")

# Save summary to a file

with open("match_summary.txt", "w") as f:
    f.write("Match Summary:\n")
    for r, p1, p2 in list_of_rounds:
        f.write(f"Round {r}: Player 1 rolled {p1} player 2 rolled {p2}\n")
