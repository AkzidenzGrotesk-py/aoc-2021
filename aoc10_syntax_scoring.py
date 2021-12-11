'''Advent of code, day 10: SYNTAX SCORING'''
from math import floor

PAIRS = {
    "{" : "}",
    "[" : "]",
    "(" : ")",
    "<" : ">",
}
SCORES = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}
SCORES_2 = [")", "]", "}", ">"]

def task_1(lines):
    '''Code for task 1:
    '''

    score = 0
    for line in lines:
        stack = []
        for char in line:
            if char in PAIRS:
                stack.append(PAIRS[char])
            elif char == stack[-1]:
                del stack[-1]
            else:
                score += SCORES[char]
                break

    return score

def task_2(lines):
    '''Code for task 2:
    '''

    scores = []
    for line in lines:
        invalid_line = False
        stack = []
        for char in line:
            if char in PAIRS:
                stack.append(PAIRS[char])
            elif char == stack[-1]:
                del stack[-1]
            else:
                invalid_line = True
                break

        if invalid_line:
            continue

        stack.reverse()
        score = 0
        for char in stack:
            score = score * 5 + SCORES_2.index(char) + 1

        scores.append(score)

    scores.sort()
    return scores[floor(len(scores) / 2)]

def main():
    '''Main function'''
    with open("aoc10_input.txt", "r", encoding = "utf-8") as file:
        contents = file.readlines()

        lines = [line.strip() for line in contents]

    print(task_1(lines))
    print(task_2(lines))

if __name__ == "__main__":
    main()
