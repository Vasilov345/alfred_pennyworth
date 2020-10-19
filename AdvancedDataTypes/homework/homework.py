from typing import List, Dict, Union, Callable
import copy

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    for student in data:
    	if student.get('name'): 
        	student['name'] = student['name'].title()
    return data

def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    dict2 = copy.deepcopy(data)
    for item in dict2:
    	for key in redundant_keys:
        	item.pop(key)
    return dict2


def task_3_find_item_via_value(data: DT, value) -> DT:
    find = [items for items in data for n in items.values() if n == value]
    return find

def task_4_return_lambda_sum_2_ints() -> DT:
    return (lambda first, second: first+second)


def task_5_append_str_to_list_and_return(input_data: List, elem: str):
    New_List = [k for k in input_data]
    New_List.append(elem)
    return New_List


def task_6_insert_function_result_into_string(func: Callable):
    return f'start {func()} finish'


def task_7_insert_2_vars_into_string(age: float, habit: str):
    return f"I have {int(age * 10) / 10} years and I love {habit.ljust(10)[:10]}"
    
