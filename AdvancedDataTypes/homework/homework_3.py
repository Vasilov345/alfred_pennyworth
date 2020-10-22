from typing import List, Dict, Union, Callable

ST = Dict[str, Union[str, int]]
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    for first_name in data:
        try:
            first_name["name"] = first_name["name"].capitalize()
        except KeyError:
            continue
    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    new_dict = []
    for dicts in data:
        new_dict.append({x: dicts[x] for x in dicts if x not in redundant_keys})
    return new_dict


def task_3_find_item_via_value(data: DT, value) -> DT:
    new_line = [dta_line for dta_line in data for key in dta_line if dta_line[key] == value]
    return new_line


def task_4_return_lambda_sum_2_ints():
    return lambda x, y: x + y


def task_5_append_str_to_list_and_return(input_data: List, elem: str):
    ap_str = input_data.copy()
    ap_str.append(elem)
    return ap_str
