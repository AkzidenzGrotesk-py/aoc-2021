'''Advent of code, day 25: SEA CUCUMBER'''
from copy import deepcopy
MAX_GEN = 1000

def task_1(seamap):
    '''Code for task 1:
    '''
    smh = len(seamap)
    smw = len(seamap[0])
    old_seamap = None
    for i in range(MAX_GEN):
        # Disguisting simulation code
        old_seamap = deepcopy(seamap)
        empty_map = [['!' for _ in r] for r in seamap]
        for y, row in enumerate(seamap):
            for x, cell in enumerate(row):
                if cell == ">":
                    if seamap[y][0 if x == smw - 1 else x+1] == ".":
                        empty_map[y][x] = "."
                        empty_map[y][0 if x == smw - 1 else x+1] = ">"
                    else:
                        empty_map[y][x] = ">"
                else:
                    if empty_map[y][x] == "!":
                        empty_map[y][x] = cell
        seamap = empty_map
        empty_map = [['!' for _ in r] for r in seamap]
        for y, row in enumerate(seamap):
            for x, cell in enumerate(row):
                if cell == "v":
                    if seamap[0 if y == smh - 1 else y+1][x] == ".":
                        empty_map[y][x] = "."
                        empty_map[0 if y == smh - 1 else y+1][x] = "v"
                    else:
                        empty_map[y][x] = "v"
                else:
                    if empty_map[y][x] == "!":
                        empty_map[y][x] = cell
        seamap = empty_map

        # Check if no movement
        if old_seamap == seamap:
            return i+1

        # Render generation
        fin = "\033[H"
        for row in seamap:
            for cell in row:
                fin += cell
            fin += "\n"
        print(f"{fin}\nGeneration #{i+1}")



def task_2(seamap):
    '''Code for task 2:
    '''
    return "Christmas has been saved! We found 50 stars!"

def main():
    '''Main function'''
    with open("aoc25_input.txt", "r", encoding = "utf-8") as file:
        seamap = [list(l.strip()) for l in file.readlines()]

    print(task_1(seamap))
    print(task_2(seamap))


if __name__ == "__main__":
    main()
