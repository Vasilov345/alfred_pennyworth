# 1. What is dictionary comprehension?
# This is the way of creating dictionaries - the dict and its contents are defined at the same time
lst = [("a", "b"), ("c", "d")]
# create a dictionary by iterating through the list where key will be the first elem of tuple, and value is the second
dict_comp = {k: v for k, v in lst}

# 2. Structure
# A dictionary comprehension takes the form {key: value for (key, value) in iterable}

# 3. Construction variations
# Comprehension basic
# create dict from list, where value will be power of 2 of list element
dict_val_power_of_2 = {x: x ** 2 for x in [1, 2, 3, 4, 5]}

# Comprehension with if statement
# create dict from list, where value will be power of 3 if it is multiple of 4 else skip
dict_comp_if = {x: x_power_3 for x in range(10) if (x_power_3 := x ** 3) % 4 == 0}

# Comprehension with if and else statement
# create dict from list where value will be power of 3 if it is multiple of 4 else value
dict_comp_if_else = {x: x ** 3 if x ** 3 % 4 == 0 else x for x in range(10)}
