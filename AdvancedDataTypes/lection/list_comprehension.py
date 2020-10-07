import random

# ********************
# List comprehension
# ********************
# 1. What is list comprehension?
# This is the way of creating lists - the list and its contents are defined at the same time (in 1 statement)
# rather than creating an empty list and adding each element to the end.
# Syntactic sugar
lst = []
# loop to make a list of 0 to 9 elements
for num in range(10):
    lst.append(num)

# list comprehension to make a list of 0 to 9 elements
lst_comp = [num for num in range(10)]

# 2. Structure
# Every list comprehension in Python includes three elements:
# expression - member itself, a call to a method, or any other valid expression that returns a value -> str(num)
# member - object or value in the list or iterable -> num
# iterable - list, set, sequence, generator, or any other object that can return its elements one at a time - range(10)
# make a list of 10 elements and convert each element to string
list_comprehension = [str(num) for num in range(10)]

# 3. Construction variations
# Comprehension with if statement
# create a list form 0 to 9 including only even elements
list_comprehension_if = [even_num for even_num in range(10) if even_num % 2 == 0]

# Comprehension with if and else statement
# create a list from 0 to 9 dividing each even elem to 2 and multiplying each odd elem to 10
list_comprehension_if_else = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]

# Comprehension with two loops
# create a list including every element from the first tuple, and then every from second tuple
list_comprehension_two_loops = [num for tup in [(1, 2, 3), (4, 5, 6)] for num in tup]


def get_weather_data():
    return random.randrange(90, 110)


# create a list from random numbers bigger than 99
# Python 3.8 - walrus operator allows to run expression while simultaneously assigning the output value to a variable.
hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]

# 4. Advantages
# less code
# easier to read and understand.  +-
# considered Pythonic (Python embraces simple, powerful tools that can be used in a wide variety of situations)
# speed (in loop - append method call, lc - specialized LIST_APPEND bytecode is generated for append)
# timeit examples to be added?

# 5. Disadvantages - not useful if
# - the logic is too long and complex
#  active_player_accounts = [player.get_account() for team in league_teams
#     if len(team.roster) > 1 for player in team.get_players()
#     if not player.is_injured()]

# - the full list is not needed - loop with break should be used
# - the list is not needed as a result - generator should be used
