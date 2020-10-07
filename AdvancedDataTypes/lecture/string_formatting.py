# ************************************
# String formatters - what and why
# ************************************
# Very often there is a need to insert some data from runtime into string:
# - user input,
# - data from files
# - filling in the same template with different data, e.g., name and surname in some application
# - logging

# This insertion may be achieved by string formatters


# ***************************
# String formatters - types
# ***************************

# Python is about giving choice:
a = "x"
b = "y"
assert a + b == "%s%s" % (a, b) == f"{a}{b}" == "{}{}".format(a, b)

# 1. "".format()
# works by putting in one or more replacement fields or placeholders — defined by a pair of curly braces {}
# and calling the str.format() method.
# This value will be passed through in the same place that your placeholder is positioned when you run the program.
print("Sammy has {} balloons.".format(5))

# We can also assign a variable to be equal to the value of a string that has formatter placeholders
open_string = "Sammy loves {}."
print(open_string.format("open source"))

# Python will replace multiple values passed through the str.format() method in order
sammy_string = "Sammy loves {} {}, and has {} {}."
print(sammy_string.format("open-source", "software", 5, "balloons"))

# Index numbers may be passed into the curly braces
str_format_by_index = "Sammy the {1} has a pet {0}!".format("shark", "pilot fish")

# Another option is using keyword arguments that are called by their keyword name:
str_format_by_keyword = "Sammy the {0} {1} a {pr}.".format("shark", "made", pr="pull request")

# More parameters may be included within the curly braces
# s for string, d to display decimal integers (10-base), and f to display floats
# {field_name:conversion} syntax
str_format_float = "Sammy ate {0:f} percent of a {1}!".format(75, "pizza")
# just one decimal place
str_format_float_places = "Sammy ate {0:.1f} percent of a pizza!".format(75.765367)
# if no fractional part needed
str_format_float_to_int = "Sammy ate {0:.0f} percent of a pizza!".format(75.765367)

# Padding variable substitution
# A number may be added to indicate field size (in terms of characters) after the colon:
# number 5 is given a character field size of 4, and the string balloons - a character field size of 16
str_padding = "Sammy has {0:4} red {1:16}!".format(5, "balloons")
# < will left-align the text in a field, ^ will center the text in the field, and > will right-align it.
str_padding_alignment = "Sammy has {0:<4} red {1:^16}!".format(5, "balloons")

# 2. New style - F-strings / Literal String Interpolation  (since Python 3.6)
# Provide a concise and convenient way to embed python expressions inside string literals for formatting.
verb = "flies"
preposition = "like"
# variables values will be inserted into string
str_f_formatting = f"Time {verb} {preposition} an arrow. Fruit {verb} {preposition} a banana."


# inserting an expression
def get_age():
    return 100


# result of get_age will be inserted into string
str_f_formating_exp = f"I am {get_age()} years old"

# 3. Old style formatting
# Strings in Python have a unique built-in operation that can be accessed with the % operator.
# "Old" - because it was technically superseded by "new style" .format() formatting in Python 3 described above
name = "boo"
str_old_style_format = 'Hello, %s' % name

# Multiple substitutions:
name = "boo"
friend_name = "foo"
# values will be inserted from brackets in order
str_old_style_format_many = 'Hey %s, there is you friend %s!' % (name, friend_name)

# Refer to variable substitutions by name - more typing, more flexibility
# values will be inserted from brackets, by keyword
print('Hey %(me)s, there is you friend %(friend)s!' % {"me": name, "friend": friend_name})

# More on this: https://docs.python.org/3.6/library/string.html#format-specification-mini-language
