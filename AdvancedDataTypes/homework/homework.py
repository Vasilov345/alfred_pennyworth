from typing import List, Dict, Union, Callable

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    for student in data:
        try:
            if student.get('name'):
                student['name'] = student['name'].capitalize()
        except KeyError:
            continue
    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    for i in data:
        try:
            for k in redundant_keys:
                i.pop(k)
        except KeyError:
            continue
    return data


def task_3_find_item_via_value(data: DT, value) -> DT:
    value = [i for i in data for v in i.values() if v == value]
    return value


def task_4_return_lambda_sum_2_ints() -> DT:
    return lambda x, y: x + y



def task_5_append_str_to_list_and_return(input_data: List, elem: str):
    new_list = input_data.copy()
    new_list.append(elem)
    return new_list


def task_6_insert_function_result_into_string(func: Callable):
    return f'start {func()} finish'


def task_7_insert_2_vars_into_string(age: float, habit: str):
    return f"I have {int(age * 10) / 10} years and I love {habit.ljust(10)[:10]}"