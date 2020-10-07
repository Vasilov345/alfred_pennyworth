import math
from typing import List, Dict, Union, Callable

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    for i in data:
        try:
            i['name'] = i['name'].capitalize()
        except KeyError:
            continue
    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    for dct in data:
        for k in redundant_keys:
            try:
                dct.pop(k)
            except KeyError:
                continue
    return data


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    res = [i for i in data for v in i.values() if v == value]
    return res


def task_4_return_lambda_sum_2_ints() -> DT:
    """
    Return lambda operator which take 2 integer params and returns their sum
    """
    return lambda a, b: a + b


def task_5_append_str_to_list_and_return(input_data: List, elem: str):
    """
    Return list with the element appended to it.
    But the list itself should not be changed
    """

    l1 = [i for i in input_data]
    l1.append(elem)
    return l1


def task_6_insert_function_result_into_string(func: Callable):
    """
    Return string, consisting of data, returned by func, surrounded by "start" and "finish"
    Rule: + operation can not be used, solution should be one-liner
    :param func: callable taking no parameters, returning string
    Examples:
        func returns "run", resulting string should be - "start run finish"
    """
    return f"start {func()} finish"


def task_7_insert_2_vars_into_string(age: float, habit: str):
    """
    Template string: "I have <first placeholder> years and I love <second placeholder>"
    where first placeholder should have only one number in fractional part,
    and second should have field size of 10 even if is is longer - only 10 positions should be occupied.
    Examples:
        "I have 10.4 years and I love cars      "
    """
    len_age = len(str(age))
    lst = []
    for i in range(len_age):
        lst.append(str(age)[i])
        if str(age)[i - 1] == '.':
            break
    str_age = "".join(lst)

    habit_lst = []
    len_habit = len(habit)
    for i in range(len_habit):
        habit_lst.append(habit[i])
        if i == 9:
            break
    str_habit = "".join(habit_lst)

    return f"I have {str_age} years and I love {str_habit:10}"
