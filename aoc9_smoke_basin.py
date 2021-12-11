'''Advent of code, day 9: SMOKE BASIN'''
from math import inf
from itertools import chain
from copy import deepcopy

temp_heightmap = []

def flood_fill(x, y):
    '''Return flood values'''
    global temp_heightmap
    if x < 0 or x >= len(temp_heightmap[0]) or y < 0 or y >= len(temp_heightmap):
        return []
    if temp_heightmap[y][x] == 9:
        return []
    if temp_heightmap[y][x] == -1:
        return []

    temp_heightmap[y][x] = -1
    return [(x, y),
        *flood_fill(x + 1, y),
        *flood_fill(x - 1, y),
        *flood_fill(x, y + 1),
        *flood_fill(x, y - 1)
    ]

def task_1(heightmap):
    '''Code for task 1:
    '''
    heightmap.insert(0, [9 for _ in heightmap[0]])
    heightmap.append([9 for _ in heightmap[0]])
    for i, _ in enumerate(heightmap):
        heightmap[i].insert(0, 9)
        heightmap[i].append(9)

    low_points = list(chain.from_iterable([
        [
            (
                x + 1, y + 1
            ) for x, cell in enumerate(line[1:-1])
            if all([
                (cell < heightmap[y+1-cy][x+1-cx]) for cx, cy in [
                    (0, 1),
                    (0, -1),
                    (1, 0),
                    (-1, 0)
                ]
            ])
        ] for y, line in enumerate(heightmap[1:-1])
    ]))


    total = sum([
        1 + heightmap[p[1]][p[0]] for p in low_points
    ])

    return [low_points, total]




def task_2(heightmap, low_points):
    '''Code for task 2:
    '''
    global temp_heightmap

    print()
    basin_sizes = []
    for i, lpoint in enumerate(low_points):
        print(f"\033[FHanding point #{i + 1}/{len(low_points)}")
        temp_heightmap = deepcopy(heightmap)
        basin_sizes.append(len(flood_fill(lpoint[0], lpoint[1])))
    basin_sizes.sort()

    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

def main():
    '''Main function'''
    with open("aoc9_input.txt", "r", encoding = "utf-8") as file:
        contents = file.readlines()

        contents = [line.strip() for line in contents]
        heightmap = [[int(i) for i in line] for line in contents]

    task1_data = task_1(heightmap)
    print(task1_data[1])
    print(task_2(heightmap, task1_data[0]))

if __name__ == "__main__":
    main()
