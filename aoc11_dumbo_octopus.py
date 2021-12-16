'''Advent of code, day 11: DUMBO OCTOPUS'''

SURROUND = [(-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0)]

def flash_octopi(octopi, has_flashed, x, y):
    '''Flash octopi, recursive'''
    if x < 0 or x > len(octopi[0]) - 1\
       or y < 0 or y > len(octopi) - 1\
       or has_flashed[y][x]:
        return

    octopi[y][x] += 1
    if octopi[y][x] > 9:
        octopi[y][x] = 0
        has_flashed[y][x] = True
        for cellp in SURROUND:
            flash_octopi(octopi, has_flashed, x + cellp[0], y + cellp[1])

def task_1(octopi, steps = 100):
    '''Code for task 1:
    '''
    flashes = 0
    for step in range(steps):
        octopi = [[i + 1 for i in line] for line in octopi]
        has_flashed = [[False for _ in line] for line in octopi]

        for y, line in enumerate(octopi):
            for x, _ in enumerate(line):
                if has_flashed[y][x]:
                    continue
                if octopi[y][x] > 9:
                    flash_octopi(octopi, has_flashed, x, y)

        # part 2
        if not sum([sum(line) for line in octopi]):
            return step + 1

        flashes += sum([sum([int(b) for b in line]) for line in has_flashed])

    return flashes

def task_2(octopi, check_for = 500):
    '''Code for task 2:
    '''

    return task_1(octopi, check_for)

def main():
    '''Main function'''
    with open("aoc11_input.txt", "r", encoding = "utf-8") as file:
        contents = file.readlines()

        octopi = [[int(i) for i in line.strip()] for line in contents]

    print(task_1(octopi))
    print(task_2(octopi))

if __name__ == "__main__":
    main()
