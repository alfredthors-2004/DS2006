import random
import copy


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

round_number = 1

# Ask for number of players
num_players = int(input("How many players? (2 or more): "))

player_info = {
    "name": "",
    "country": "",
    "email": "",
    "dice_sides": 0,
    "wins": 0,
}

# Store players in a list
players = []
round_history = []
for i in range(num_players):
    player = copy.deepcopy(player_info)
    player["name"] = input(f"What is the name of Player {i+1}?")
    player["email"] = input(f"What is the e-mail of Player {i+1}?")
    player["country"] = input(f"What is the country of Player {i+1}?")
    player["dice_sides"] = int(
        input(f"How many sides on {player['name']}'s dice? "))
    players.append(player)

# Play until someone wins 3 times
while max(p["wins"] for p in players) < 3:
    input(f"\nRound {round_number}: Press ENTER to roll the dice...")

    rolls = []
    for i, player in enumerate(players):
        roll = rollDice(player["dice_sides"])
        rolls.append(roll)
        print(f"{player['name']} rolled: {roll}")

    max_roll = max(rolls)
    winners = [i for i, r in enumerate(rolls) if r == max_roll]

   # Give a point to all players with the highest roll

    for w in winners:
        players[w]["wins"] += 1

    if len(winners) == 1:
        print(f"{players[winners[0]]['name']} wins this round!")
    else:
        print("It's a tie! The following players get a point:",
              ", ".join([players[w]['name'] for w in winners]))

    # Track round history
    round_info = {
        "round": round_number,
        "rolls": {player['name']: roll for player, roll in zip(players, rolls)},
        "winners": [players[w]['name'] for w in winners]
    }
    round_history.append(round_info)

    # Show current score
    print("Score:", " | ".join(
        [f"{p['name']} = {p['wins']}" for p in players]))
    round_number += 1

# Announce the overall winner
winner = max(players, key=lambda p: p["wins"])
print(f"\n{winner['name']} from {winner['country']} "
      f"is the newest Battle of Dices Champion!!")

# Save results to a file
filename = input("ENter the filename to save the results: ")
with open(filename, "w") as file:  # "w" = write mode
    # Player Information:
    file.write("Player Information:\n")

    # Saves each player information using python automatically concatenation
    # of adjacent strings:
    for each_player in players:
        file.write(
            f"Name: {each_player['name']}\n"
            f"* E-mail: {each_player['email']}\n"
            f"* Country: {each_player['country']}\n"
            f"* Wins: {each_player['wins']}\n\n"
        )

    # ... still in with open
    file.write("\nGame rounds:\n")

    # Round history
    for rh in round_history:
        rolls_str = ", ".join(
            [f"{name} rolled {roll}" for name, roll in rh["rolls"].items()]
        )
        winners_str = ", ".join(rh["winners"])
        file.write(
            f"Round {rh['round']}: {rolls_str} | Winner(s): {winners_str}\n"
        )

    # Champion
    winner = max(players, key=lambda p: p["wins"])
    file.write(
        f"\nChampion: {winner['name']} from {winner['country']}\n"
    )

print("\nGame over! Results saved successfully.")
