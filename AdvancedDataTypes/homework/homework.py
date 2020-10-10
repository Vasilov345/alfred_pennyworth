from typing import List, Dict, Union, Callable


def task_1_fix_names_start_letter(dicti):
    for di in dicti:
        if 'name' in di.keys():
            if di['name'].lower():
                di['name'] = di['name'].title()
    return dicti

def task_2_remove_dict_fields(data, redundant_keys):
    for i in data:
        for j in redundant_keys:
            del i[j]
    return data


def task_3_find_item_via_value(data, value):
    lists = []
    x = 0
    for i in data:
        if i['name'] == value or i['age'] == value:
            lists.append(data[x])
        else:
            x += 1
    return lists

def task_4_return_lambda_sum_2_ints():
    g = (lambda a, b: a + b)
    return g


def task_5_append_str_to_list_and_return(data_list, elem_str):
    new_list = [i for i in data_list]
    new_list.append(elem_str)
    return new_list


def task_6_insert_function_result_into_string(func: Callable):
     return f'start {func()} finish'
     

def task_7_insert_2_vars_into_string(age, habit):
    age = int(age * 10) / 10
    habit = habit[:10]
    if len(habit) >= 10:
        x = f'I have {age} years and I love {habit}'
        return x
    else:
        x = f'I have {age} years and I love {habit:10}'
        return x

