'''Advent of code, day 24: ARITHMETIC LOGIC UNIT'''
from math import floor
from functools import lru_cache
from my_helper import flatten

def execute_alu(code, input_stream):
    '''Manually interpreting every line of ALU, not efficient for repeated actions'''
    mem = {"x":0,"y":0,"z":0,"w":0}
    istream = input_stream
    for line in code:
        cmds = line.split(" ")
        '''Python < 3.9 version--'''
        if cmds[0] == "inp":
            if len(input_stream) == 0:
                mem[cmds[1]] = input("Input stream empty, please enter a value manually: ")
            else:
                mem[cmds[1]] = int(istream.pop(0))
        else:
            val_a = int(mem[cmds[1]])
            val_b = int(mem[cmds[2]]) if cmds[2] in mem else int(cmds[2])
            if cmds[0] == "add":
                mem[cmds[1]] = val_a + val_b
            elif cmds[0] == "mul":
                mem[cmds[1]] = val_a * val_b
            elif cmds[0] == "div":
                mem[cmds[1]] //= val_b
            elif cmds[0] == "mod":
                mem[cmds[1]] = val_a % val_b
            elif cmds[0] == "equ":
                mem[cmds[1]] = int(val_a == val_b)
        '''Python 3.10 version---
        match cmds:
            case "inp", var:
                if len(input_stream) == 0:
                    mem[var] = input("Input stream empty, please enter a value manually: ")
                else:
                    mem[var] = int(istream.pop(0))
            case oper, var_a, var_b:
                val_a = int(mem[var_a])
                val_b = int(mem[var_b]) if var_b in mem else int(var_b)
                match oper:
                    case "add":
                        mem[var_a] = val_a + val_b
                    case "mul":
                        mem[var_a] = val_a * val_b
                    case "div":
                        mem[var_a] //= val_b
                    case "mod":
                        mem[var_a] = val_a % val_b
                    case "equ":
                        mem[var_a] = int(val_a == val_b)'''

    return mem


def task_1(ax, dz, ay):
    '''Code for task 1:
    '''
    def calc_step(ins_step, z, w):
        '''Run section operation'''
        x = ax[ins_step] + (z % 26)
        z //= dz[ins_step]
        if x != w:
            z = z * 26 + w + ay[ins_step]
        return z

    @lru_cache(maxsize = None)
    def recur_search(ins_step, z):
        '''Find every character reaching criteria and recur to the next char'''
        if ins_step == 14:
            return [""] if not z else []
        if z > zmax[ins_step]:
            return []
        cx = ax[ins_step] + z % 26
        w_pos = [cx] if 1 <= cx < 10 else range(1,10)
        return flatten([
            [
                str(w) + x
                for x in recur_search(ins_step + 1,
                    calc_step(ins_step, z, w))
            ] for w in w_pos
        ])

    # Maximum possible values of Z
    zmax = [
        26 ** len\
            ([x for x, _ in enumerate(dz)
                if dz[x] == 26 and x >= i])
        for i, _ in enumerate(dz)
    ]

    return map(int, recur_search(0, 0))

def task_2(pos_solu):
    '''Code for task 2:
    '''
    return min(pos_solu)

def main():
    '''Main function'''
    with open("aoc24_input.txt", "r", encoding = "utf-8") as file:
        contents = [l.strip() for l in file.readlines()]
        tot = [[] for _ in range(3)]
        appl = [5, 4, 15]
        for i, line, in enumerate(contents):
            if i % 18 in appl:
                tot[appl.index(i % 18)].append(int(line.split()[2]))

        if any(i != 14 for i in map(len, tot)):
            print("bad input.")

    solutions = list(task_1(*tot))
    print(max(solutions))
    print(task_2(solutions))

if __name__ == "__main__":
    main()
