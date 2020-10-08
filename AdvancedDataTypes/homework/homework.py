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
    pass


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    pass


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    pass


def task_4_return_lambda_sum_2_ints() -> DT:
    """
    Return lambda operator which take 2 integer params and returns their sum
    """
    pass


def task_5_append_str_to_list_and_return(input_data: List, elem: str):
    """
    Return list with the element appended to it.
    But the list itself should not be changed
    """
    pass


def task_6_insert_function_result_into_string(func: Callable):
    """
    Return string, consisting of data, returned by func, surrounded by "start" and "finish"
    Rule: + operation can not be used, solution should be one-liner
    :param func: callable taking no parameters, returning string
    Examples:
        func returns "run", resulting string should be - "start run finish"
    """


def task_7_insert_2_vars_into_string(age: float, habit: str):
    """
    Template string: "I have <first placeholder> years and I love <second placeholder>"
    where first placeholder should have only one number in fractional part,
    and second should have field size of 10 even if is is longer - only 10 positions should be occupied.
    Examples:
        "I have 10.4 years and I love cars      "
    """
