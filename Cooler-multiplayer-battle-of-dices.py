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


print("Welcome to Battle of Dices!")

# Ask for number of players
num_players = int(input("How many players? (2 or more): "))

# Ask for nicknames
player_names = []
for i in range(num_players):
    name = input(f"Enter nickname for Player {i+1}: ")
    player_names.append(name)

player_wins = [0] * num_players
round_number = 1

# Ask for dice sides for each player
dice_sides = []
for i in range(num_players):
    sides = int(input(f"How many sides for {player_names[i]}'s dice? "))
    dice_sides.append(sides)

# Play until someone wins 3 times
while max(player_wins) < 3:
    input(f"\nRound {round_number}: Press ENTER to roll the dice...")

    rolls = []
    for i in range(num_players):
        roll = rollDice(dice_sides[i])
        rolls.append(roll)
        print(f"{player_names[i]} rolled: {roll}")

    max_roll = max(rolls)
    winners = [i for i, r in enumerate(rolls) if r == max_roll]

   # Give a point to all players with the highest roll

    for w in winners:
        player_wins[w] += 1
    if len(winners) == 1:
        print(f"{player_names[winners[0]]} wins this round!")
    else:
        print("It's a tie! The following players get a point:",
              ", ".join([player_names[w] for w in winners]))

    # Show current score
    print("Score:", " | ".join(
        [f"{player_names[i]} = {w}" for i, w in enumerate(player_wins)]))
    round_number += 1

# Announce the overall winner
winner = player_wins.index(max(player_wins))
print(f"\n{player_names[winner]} is the newest Battle of Dices Champion!!")
