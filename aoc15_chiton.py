'''Advent of code, day 15: CHITON'''
from math import inf
from itertools import chain
from copy import deepcopy

def minimum_cost(grid):
    '''Minimum cost of grid'''
    row = len(grid)
    col = len(grid[0])

    for i in range(1, row):
        grid[i][0] += grid[i - 1][0]

    for j in range(1, col):
        grid[0][j] += grid[0][j - 1]

    for i in range(1, row):
        for j in range(1, col):
            mins = [grid[i - 1][j], grid[i][j - 1],]
            grid[i][j] += min(mins)

    return grid[-1][-1] - grid[0][0]

def inc_grid(grid, inc):
    '''Increment a grid by a value, wrapping when past 9'''
    return [[c + inc if c < (10 - inc) else inc - (9 - c) for c in l] for l in grid]

def task_1(grid):
    '''Code for task 1:
    '''
    return minimum_cost(grid)

def task_2(grid):
    '''Code for task 2:
    '''
    mods = [[(j + i)  for j in range(5)] for i in range(5)]
    ngrid = [
        [
            inc_grid(grid, mods[i][j])
            for j in range(5)
        ] for i in range(5)
    ]

    final_grid = [
        list(chain.from_iterable(
            [
                ngrid[
                    int(f'{rown:03}'[0])
                ][i][rown % len(grid[0])] for i in range(5)
            ]
        )) for rown in range(len(grid) * 5)
    ]
    cost = minimum_cost(final_grid)

    return cost



def main():
    '''Main function'''
    with open("aoc15_input.txt", "r", encoding = "utf-8") as file:
        contents = file.readlines()
        grid = [[int(c) for c in l.strip()] for l in contents]
        copy_grid = deepcopy(grid)

    print(task_1(grid))
    print(task_2(copy_grid))

if __name__ == "__main__":
    main()

