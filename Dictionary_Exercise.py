lottery_numbers = {13, 21, 22, 5, 8}


"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players
"""
players = [
    {
        'name': 'Aparna',
        'numbers': {5, 7, 20, 35}
    },
    {
        'name': 'Abhishek',
        'numbers': {9, 13, 27, 41}
    }
]

"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers. We still cannot use f-strings in this exercise.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""
p1_right_numbers = lottery_numbers.intersection(players[0].get('numbers'))
p1_name = players[0]['name']

p2_right_numbers = lottery_numbers.intersection(players[1].get('numbers'))
p2_name = players[1]['name']

# print(f'Player {p1_name} got {len(p1_right_numbers)} right')
# print(f'Player {p2_name} got {len(p2_right_numbers)} right')

print('Player {} got {} right'.format(p1_name, len(p1_right_numbers)))
print('Player {} got {} right'.format(p2_name, len(p2_right_numbers)))
