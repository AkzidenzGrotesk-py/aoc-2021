'''Advent of code, day 7: THE TREACHERY OF WHALES'''
from math import inf

def task_1(pos):
    '''Code for task 1:
    '''

    lowest_cost = inf
    for i, point in enumerate(pos):
        total_fuel_cost = 0
        for j, check_point in enumerate(pos):
            if i == j:
                continue
            total_fuel_cost += abs(check_point - point)
        if total_fuel_cost < lowest_cost:
            lowest_cost = total_fuel_cost

    return lowest_cost

def task_2(pos):
    '''Code for task 2:
    '''

    lowest_cost = inf
    for i, point in enumerate(pos):
        total_fuel_cost = 0
        for j, check_point in enumerate(pos):
            if i == j:
                continue
            total_fuel_cost += sum([x for x in range(1, abs(check_point - point) + 1)])
        if total_fuel_cost < lowest_cost:
            lowest_cost = total_fuel_cost

    return lowest_cost

def main():
    '''Main function'''
    with open("aoc7_input.txt", "r", encoding = "utf-8") as file:
        contents = file.readlines()

        # Convert data in form "a,b,c,d,..."
        pos = contents[0].split(",")
        pos = [int(i) for i in pos]

    print(task_1(pos))
    print(task_2(pos))

if __name__ == "__main__":
    main()
