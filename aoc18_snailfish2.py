'''Advent of code, day 18: SNAILFISH'''
# Second solution using string manipulation

from math import floor, ceil, inf
from re import finditer, findall
from copy import deepcopy

def rreplace(string, text, replacewith, num):
    '''Replace from the right-left'''
    return replacewith.join(string.rsplit(text, num))

def explode_sfn(sfn: str) -> (bool, str):
    '''Explode the first occurance'''
    for low in finditer(r"\[\d+\,\d+\]", sfn):
        depth = sfn[:low.start()].count("[") - sfn[:low.start()].count("]")
        if depth >= 4:
            left_num, right_num = sfn[low.start():low.end()].split(",")
            left_num, right_num = left_num[1:], right_num[:-1]
            left, right = sfn[:low.start()], sfn[low.end():]
            left_sect = findall(r"\d+[^0-9]+$", left)
            right_sect = findall(r"^[^0-9]+\d+", right)
            if left_sect:
                ln = findall(r"\d+", left_sect[0])[0]
                left = rreplace(
                    left,
                    left_sect[0],
                    left_sect[0].replace(ln,
                    str(int(ln) + int(left_num))),
                    1
                )
            if right_sect:
                rn = findall(r"\d+", right_sect[0])[0]
                right = right.replace(
                    right_sect[0],
                    right_sect[0].replace(rn,
                    str(int(rn) + int(right_num))),
                    1
                )
            sfn = "0".join([left, right])
            return True, sfn
    return False, sfn

def split_sfn(sfn: str) -> (bool, str):
    '''Split the first number > 9'''
    for big in finditer(r"[0-9]{2,3}", sfn):
        text = sfn[big.start():big.end()]
        sfn = sfn.replace(
            text,
            f"[{floor(int(text) / 2)},{ceil(int(text) / 2)}]",
            1
        )
        return True, sfn
    return False, sfn


def add_sfn(sfn1: str, sfn2: str) -> str:
    '''Add and reduce two snailfish numbers'''
    sfn = f"[{sfn1},{sfn2}]"
    breaker_loop = False
    while 1:
        exploded, sfn = explode_sfn(sfn)
        if not exploded:
            splitted, sfn = split_sfn(sfn)
            if not splitted:
                if breaker_loop:
                    break
                breaker_loop = True
                continue
        breaker_loop = False
    return sfn

def magnitude_sfn(sfn: str) -> int:
    '''Get the magnitude of a snailfish number'''
    return eval(sfn.replace("[", "(3*").replace("]", "*2)").replace(",", "+").replace("+*", "*"))

def task_1(sfnumbers):
    '''Code for task 1:
    '''
    copy_sfnumbers = deepcopy(sfnumbers)
    for i, _ in enumerate(copy_sfnumbers[:-1]):
        copy_sfnumbers[i + 1] = \
            add_sfn(copy_sfnumbers[i], copy_sfnumbers[i + 1])

    return magnitude_sfn(copy_sfnumbers[-1])

def task_2(sfnumbers):
    '''Code for task 2:
    '''
    highest = -inf
    for sfn1 in sfnumbers:
        for sfn2 in sfnumbers:
            magnitude = \
                magnitude_sfn(
                    add_sfn(sfn1, sfn2)
                )
            if magnitude > highest:
                highest = magnitude
    return highest

def main():
    '''Main function'''
    with open("aoc18_input.txt", "r", encoding = "utf-8") as file:
        contents = file.readlines()
        sfnumbers = [l.strip() for l in contents]

    print(task_1(sfnumbers))
    print(task_2(sfnumbers))

if __name__ == "__main__":
    main()
