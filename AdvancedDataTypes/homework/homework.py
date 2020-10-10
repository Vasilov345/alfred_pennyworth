from typing import List, Dict, Union, Callable

ST = Dict[str, Union[str, int]]
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    for first_name in data:
        try:
            first_name["name"] = first_name["name"].capitalize()
        except KeyError:
            "name"
    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    for data_member in data:
        for k in redundant_keys:
            del data_member[k]
    return data


def task_3_find_item_via_value(data: DT, value) -> DT:
    newline_cinema = []
    for dta_line in data:
        for key in dta_line:
            if dta_line[key] == value:
                newline_cinema.append(dta_line)
    return newline_cinema


def task_4_return_lambda_sum_2_ints():
    return lambda x, y: x + y


def task_5_append_str_to_list_and_return(input_data: List, elem: str):
    for jack in elem:
        return input_data + [jack]


def task_6_insert_function_result_into_string(func: Callable):
    return f'start {func()} finish'


def task_7_insert_2_vars_into_string(age: float, habit: str):
    return f'I have {int(age * 10) / 10} years and I love {habit.ljust(10)[:10]}'
