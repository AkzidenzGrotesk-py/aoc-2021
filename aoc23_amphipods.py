# UNSOLVED with code, solved in other means
'''Advent of code, day 23: AMPHIPODS'''
from copy import deepcopy

COSTS = {'A':1, 'B':10, 'C':100, 'D':1000}
INDEXES = lambda c: ord(c) - 65
WIN = [['', '', 'X', '', 'X', '', 'X', '', 'X', '', ''], ['AA', 'BB', 'CC', 'DD']]

def task_1(hallmap):
    '''Code for task 1:
    '''

    winning = []
    explo = []
    Q = [(0, hallmap)]
    while Q != []:
        v = Q.pop(0)
        print(f"\033[FChecking {v} / {len(Q)}")
        if v[1] == WIN:
            winning.append(v)
            print(f"-- WINNING POSITION: {v[0]} -- / {len(Q)}", end ="")
        posb = []
        for j, hall in enumerate(v[1][1]):
            iic = 0
            if hall[0] != " ":
                char = hall[0]
            else:
                if hall[1] != " ":
                    char = hall[1]
                    if char in WIN[1][j]:
                        continue
                    iic = 1
                else:
                    continue
            if hall == WIN[1][INDEXES(char)]:
                continue
            for i, hlp in enumerate(v[1][0]):
                if hlp == '':
                    e_pos = [(j+1)*2, i]
                    e_pos.sort()
                    for k in e_pos:
                        if k not in ['', 'X']:
                            continue
                    copymap = deepcopy(v[1])
                    copymap[0][i] = char
                    copymap[1][j] = copymap[1][j].replace(char, " ", 1)
                    cost = (abs(((j+1)*2)-i)+1+iic)*COSTS[char]
                    newstate = (v[0] + cost, copymap)
                    posb.append(newstate)
        for i, hlp in enumerate(v[1][0]):
            if hlp in COSTS:
                j = INDEXES(hlp)
                dest_hall = v[1][1][j]
                if dest_hall in ["  ", f" {hlp}"]:
                    e_pos = [i, (j+1)*2]
                    e_pos.sort()
                    for k in e_pos:
                        if k not in ['', 'X']:
                            continue
                    copymap = deepcopy(v[1])
                    copymap[0][i] = ''
                    iic = 0
                    if dest_hall == "  ":
                        copymap[1][j] = f" {hlp}"
                        iic += 2
                    else:
                        copymap[1][j] = f"{hlp*2}"
                        iic += 1
                    cost = (abs(((j+1)*2)-i)+1+iic)*COSTS[char]
                    newstate = (v[0] + cost, copymap)
                    posb.append(newstate)

        pposb = []
        for state in posb:
            if state in Q:
                existing = Q.index(state)
                if Q[existing][0] > state[0]:
                    Q[existing][0] = state[0]
            else:
                pposb.append(state)

        Q.extend(pposb)

    print(winning)
    costs = [e[0] for e in winning]
    return min(costs)

def task_2(hallmap):
    '''Code for task 2:
    '''

def main():
    '''Main function'''
    with open("aoc23_input.txt", "r", encoding = "utf-8") as file:
        contents = file.read()
        hallway = ['' for _ in range(contents.count("."))]
        for i in range(2, 9, 2):
            hallway[i] = "X"
        striplam = lambda st: st.strip()
        let_pos = "".join(map(striplam,contents.split("\n")[2:4])).replace("#","")
        letters = [
            "".join([let_pos[z] for z in range(i, 8, 4)])
            for i in range(4)]
        hallmap = [hallway, letters]

    print(task_1(hallmap))
    print(task_2(hallmap))

if __name__ == "__main__":
    main()
