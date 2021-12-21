'''Advent of code, day 2: DIVE!'''
# Solution which involves generating beauty.

def task_1(directions):
    '''Code for task 1:
    '''
    with open("direction_calc.py", "w", encoding = "utf-8") as file:
        file.write(
            "".join(["d=0;h=0;",
            directions\
                .replace("aforward ", "")\
                .replace("forward ", "h+=")\
                .replace("down ", "d+=")\
                .replace("up ","d-=")])
        )
    from direction_calc import h, d
    return h*d

def task_2(directions):
    '''Code for task 2:
    '''
    with open("direction_calc2.py", "w", encoding = "utf-8") as file:
        file.write(
            "".join(["d=0;h=0;a=0;",
            directions\
                .replace("aforward ", "d+=a*")\
                .replace("forward ", "h+=")\
                .replace("down ", "a+=")\
                .replace("up ","a-=")])
        )
    from direction_calc2 import h, d
    return h*d

def main():
    '''Main function'''
    with open("aoc2_input.txt", "r", encoding = "utf-8") as file:
        directions = ";".join([
            f"{l};a{l}" if l[0] == "f" else l for l in file.readlines()
        ])

    print(task_1(directions))
    print(task_2(directions))

if __name__ == "__main__":
    main()
