'''Advent of code, day 22: REACTOR REBOOT'''
from math import prod
from copy import deepcopy
from itertools import pairwise
from my_helper import flatten

def task_1(procedure):
    '''Code for task 1:
    '''
    on_squares = set()
    for step in procedure:
        cube = set(
            (x, y, z)
            for x in range(step[0], step[1])
            for y in range(step[2], step[3])
            for z in range(step[4], step[5])
        )
        if step[6]:
            on_squares.update(cube)
        else:
            for pos in cube:
                on_squares.discard(pos)

    return len(on_squares)

def task_2(procedure):
    '''Code for task 2:
    '''
    final = []
    pairs6 = list(pairwise(range(6)))[::2]
    for cube in procedure:
        recalc_cubes = [cube]
        for i, item in enumerate(final):
            if all(
                    cube[b] > item[a] and cube[a] < item[b]
                    for a, b in pairs6
                ):
                # resize accordingly
                for pa, pb in pairs6:
                    if item[pa] < cube[pa]:
                        newitem = deepcopy(item)
                        newitem[pb] = cube[pa]
                        item[pa] = cube[pa]
                        recalc_cubes.append(newitem)
                    if item[pb] > cube[pb]:
                        newitem = deepcopy(item)
                        newitem[pa] = cube[pb]
                        item[pb] = cube[pb]
                        recalc_cubes.append(newitem)
            else:
                recalc_cubes.append(item)
        final = recalc_cubes

    total = [
        prod([cube[b] - cube[a] for a, b in pairs6])
        for cube in final if cube[6]
    ]

    return sum(total)


def main():
    '''Main function'''
    with open("aoc22_input.txt", "r", encoding = "utf-8") as file:
        contents = file.readlines()
        left1 = lambda tup: (int(tup[0]), int(tup[1])+1)
        proced = \
            [
                [
                    *flatten([
                        left1(z[2:].split(".."))
                        for z in l.split()[1].split(",")
                    ]), 1 if l.split()[0] == 'on' else 0
                ] for l in contents
            ]

    print(task_1(proced[:20]))
    print(task_2(proced))

if __name__ == "__main__":
    main()
