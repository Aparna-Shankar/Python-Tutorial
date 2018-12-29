# Find the player with the most correct numbers and print out their name and winnings

import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(list(range(22)), 6))

players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

print(lottery_numbers)
p_name = []
winnings = []

for each_player in players:
    p_name.append(each_player['name'])
    matched_numbers = len(lottery_numbers & each_player['numbers'])
    winnings.append(100 ** matched_numbers)

# comprehend a dictionary with the name and winning of each player
player_winnings = dict(zip(p_name, winnings))

max_win = max(winnings)

for name, win_amt in player_winnings.items():
    if win_amt == max_win:
        print(f'{name} won {win_amt}.')


# top_player = players[0]
# for each_player in players:
#     matched_numbers = len(lottery_numbers & each_player['numbers'])
#     if matched_numbers > len(lottery_numbers & top_player['numbers']):
#         top_player = each_player

# # Calculate the winnings
# winnings = 100 ** len(lottery_numbers & top_player['numbers'])

# print('{} won {}!'.format(top_player['name'], winnings))
