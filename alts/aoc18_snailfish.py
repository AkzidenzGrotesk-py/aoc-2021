'''Advent of code, day 18: SNAILFISH'''

# Basically a Python version of the solution here:
# https://www.reddit.com/r/adventofcode/comments/rjekr4/2021_day_18_simpler_solution_with_data_structure/
# Still many of my own personal implementations though!

from math import floor, ceil, inf
from copy import deepcopy

def opt_chain(value, index):
    '''A bad implementation of the .? operator in JavaScript'''
    if isinstance(value, dict) and index in value:
        return value[index]
    return None

def to_value(node):
    '''Change from {} to []'''
    if opt_chain(node, "value") == 0:
        return 0
    return list(map(to_value, node))\
        if opt_chain(node, "value") is None\
        else opt_chain(node, "value")

def to_tree(array):
    '''Convert a value:depth type snailfish number to a tree'''
    if len(array) == 2:
        return to_value(array)
    for i, item in enumerate(array[:-1]):
        v1, d1, v2, d2 = \
            item["value"], item["depth"],\
            array[i + 1]["value"], array[i + 1]["depth"]
        if d1 == d2:
            return to_tree([
                *array[0:i],
                {"value" : [v1, v2], "depth" : d1 - 1},
                *array[i+2:]
            ])

    return array

def magnitude_sfn(value):
    '''Get the magnitude of a tree type snailfish number'''
    if isinstance(value, int):
        return value

    return 3 * magnitude_sfn(value[0]) + 2 * magnitude_sfn(value[1])

def list_to_depths(sfn: list, depth: int = 0) -> list:
    '''Convert snailfish lists into snailfish depths'''
    final = []
    if isinstance(sfn[0], int):
        final.append([sfn[0], depth])
    if isinstance(sfn[0], list):
        vals = list_to_depths(sfn[0], depth + 1)
        if isinstance(vals[0], list):
            final.extend(vals)
        else:
            final.append(vals)

    if isinstance(sfn[1], int):
        final.append([sfn[1], depth])
    if isinstance(sfn[1], list):
        vals = list_to_depths(sfn[1], depth + 1)
        if isinstance(vals[1], list):
            final.extend(vals)
        else:
            final.append(vals)

    return final

def explode_sfn(sfn: list) -> bool:
    '''Explode first explodable in a snailfish number'''
    for i, (value, depth) in enumerate(sfn[:]):
        if depth >= 4:
            if i > 0:
                sfn[i - 1][0] += value
            if i < len(sfn) - 2:
                sfn[i + 2][0] += sfn[i + 1][0]
            sfn[i:i+2] = [[0, depth - 1]]
            return True
    return False

def split_sfn(sfn: list) -> bool:
    '''Split the first splittable in a snailfish number'''
    for i, (value, depth) in enumerate(sfn[:]):
        if value > 9:
            sfn[i:i+1] = [[
                floor(value / 2),
                depth + 1],[
                ceil(value / 2),
                depth + 1]]
            return True
    return False

def reduce_sfn(sfn: list) -> list:
    '''Reduce a snailfish number'''
    while explode_sfn(sfn) or split_sfn(sfn):
        pass
    return sfn

def add_sfn(sfn: list, sfn2: list) -> list:
    '''Add two snailfish numbers and reduce'''
    copy_sfn = deepcopy(sfn)
    copy_sfn.extend(sfn2)
    nsfn = [[n[0], n[1] + 1] for n in copy_sfn]
    return reduce_sfn(nsfn)


def task_1(sfnumbers):
    '''Code for task 1:
    '''
    copy_sfnumbers = deepcopy(sfnumbers)
    for i, sfn in enumerate(copy_sfnumbers):
        if i >= len(copy_sfnumbers) - 1:
            continue
        added = add_sfn(sfn, copy_sfnumbers[i + 1])
        copy_sfnumbers[i + 1] = added

    return magnitude_sfn(to_tree([{"value" : i[0], "depth" : i[1]} for i in copy_sfnumbers[-1]]))

def task_2(sfnumbers):
    '''Code for task 2:
    '''
    highest = -inf
    for sfn1 in sfnumbers:
        for sfn2 in sfnumbers:
            magnitude = \
                magnitude_sfn(
                    to_tree(
                        [{"value" : i[0], "depth" : i[1]}
                        for i in add_sfn(sfn1, sfn2)]
                    )
                )
            if magnitude > highest:
                highest = magnitude
    return highest

def main():
    '''Main function'''
    with open("aoc18_input.txt", "r", encoding = "utf-8") as file:
        contents = file.readlines()
        # Evaluate into list and convert into depths type
        sfnumbers = [list_to_depths(eval(l)) for l in contents]

    print(task_1(sfnumbers))
    print(task_2(sfnumbers))

if __name__ == "__main__":
    main()
