import string
import random

def generate_alphabet():
    keys_list = []
    run_list = []
    x = 1
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    while x <= len(alphabet_list):
        run_num = random.randint(0, 100)
        if run_num in run_list:
            continue
        run_list.append(run_num)
        run_list = list(tuple(run_list))
        x += 1
    keys_alphabet_list = dict(zip(alphabet_list, run_list))
    for x in alphabet_list:
        keys_list.append({x:keys_alphabet_list[x]})
    return keys_list


def sort_alphabet(l2):
    l3 = []
    s = {}
    sorted_alphabet = []
    for k in l2:
        l3.append(k)
        for j, d in k.items():
            s[j] = d
    s = {k: v for k, v in sorted(s.items(), key=lambda item: item[1])}
    for x in s:
        sorted_alphabet.append({x: s[x]})
    print(sorted_alphabet)
    return sorted_alphabet