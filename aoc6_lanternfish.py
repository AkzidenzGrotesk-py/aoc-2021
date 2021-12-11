'''Advent of code, day 6: LANTERNFISH'''
from collections import Counter

def task_1(ages, generations = 80):
    '''Code for task 1:
    - Lanternfish have ages x
    - If x is 0, reset age to 6 and add a fish with age 8
    How many lanternfish at generation 80?
    '''

    counter_ages = Counter(ages)

    for _ in range(generations):
        next_counter = Counter({1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0})
        for c in counter_ages:
            if c > 0:
                next_counter[c - 1] += counter_ages[c]
            elif c == 0:
                next_counter[6] += counter_ages[c]
                next_counter[8] += counter_ages[c]
        counter_ages = next_counter

    return counter_ages.total()

def task_2(ages):
    '''Code for task 2:
    How many lanternfish at generation 256?
    '''

    return task_1(ages, 256)

def main():
    '''Main function'''
    with open("aoc6_input.txt", "r", encoding = "utf-8") as file:
        contents = file.readlines()

        # Convert data in form "a,b,c,d,..."
        ages = contents[0].split(",")
        ages = [int(i) for i in ages]

    print(task_1(ages))
    print(task_2(ages))

if __name__ == "__main__":
    main()
