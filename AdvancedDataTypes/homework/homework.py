from typing import List, Dict, Union, Callable

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:

    for n in data:
        if not n.get('name') is None:
            s2=str.capitalize(n.get("name"))
            n["name"]=s2
    return data



def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:

    if type(redundant_keys) is str:
        for n in data:
            del n[redundant_keys]
    if type(redundant_keys) is list:
        for n in data:
            for k in redundant_keys:
                del n[k]
    return data
task_2_remove_dict_fields([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')


def task_3_find_item_via_value(data: DT, value) -> DT:
    find=[items for items in data for v in items.values() if v == value]
    return find



def task_4_return_lambda_sum_2_ints() -> DT:
    return(lambda x,y:x+y)



def task_5_append_str_to_list_and_return(input_data: List, elem: str):
    List=[n for n in input_data]
    List.append(elem)
    return List


def task_6_insert_function_result_into_string(func: Callable):
    return f"start {func()} finish"


def task_7_insert_2_vars_into_string(age: float, habit: str):
    return f"I have {int(age * 10)/ 10} years and I love {habit.ljust(10)[:10]}"