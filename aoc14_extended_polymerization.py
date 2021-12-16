'''Advent of code, day 14: EXTENDED POLYMERIZATION'''
from itertools import pairwise
from collections import Counter
from time import time

def task_1(start_pos, insertion_rules, num_times = 10):
    '''Code for task 1:
    '''

    pairs = Counter(["".join(p) for p in pairwise(start_pos)])
    
    for _ in range(num_times):
        new_pairs = Counter()
        for pair in pairs:
            pair_val = pairs[pair]
            if pair in insertion_rules:
                pair_rule = insertion_rules[pair]
                new_pairs[pair_rule[0]] += pair_val
                new_pairs[pair_rule[1]] += pair_val
        pairs = new_pairs

    for pair in pairs:
        counts[f"<{pair[0]}"] += pairs[pair]
        counts[f">{pair[1]}"] += pairs[pair]

    new_counts = Counter({
        pair[1] : max(counts[pair], counts["<" + pair[1]])
        for pair in counts
        if pair[0] == ">"
    })

    return max(new_counts.values()) - min(new_counts.values())

def task_2(start_pos, insertion_rules):
    '''Code for task 2:
    '''
    return task_1(start_pos, insertion_rules, 40)

def main():
    '''Main function'''
    with open("aoc14_input.txt", "r", encoding = "utf-8") as file:
        contents = file.readlines()

        start_pos = contents[0].strip()
        insertion_rules = [line.strip().split(" -> ") for line in contents[2:]]
        insertion_rules = {rule[0] : [rule[0][0] + rule[1], rule[1] + rule[0][1]] for rule in insertion_rules}

    print(task_1(start_pos, insertion_rules))
    print(task_2(start_pos, insertion_rules))

if __name__ == "__main__":
    main()
