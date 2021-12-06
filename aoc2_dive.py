'''Advent of code, day 2: DIVE!'''

def task_1(directions):
    '''Code for task 1:
    - forward X increases the horizontal position by X units.
    - down X increases the depth by X units.
    - up X decreases the depth by X units.

    Calculate the horizontal position and depth you would have after following the planned course.
    What do you get if you multiply your final horizontal position by your final depth?'''
    position, depth = 0, 0

    for command in directions:
        match command:
            case "forward", units:
                position += int(units)
            case "down", units:
                depth += int(units)
            case "up", units:
                depth -= int(units)
            case _:
                print("[ERROR] unrecognized command.")

    return position * depth

def task_2(directions):
    '''Code for task 2:
    - down X increases your aim by X units.
    - up X decreases your aim by X units.
    - forward X does two things:
        - It increases your horizontal position by X units.
        - It increases your depth by your aim multiplied by X.

    Using this new interpretation of the commands, calculate the horizontal position and
    depth you would have after following the planned course.
    What do you get if you multiply your final horizontal position by your final depth?'''
    position, depth, aim = 0, 0, 0

    for command in directions:
        match command:
            case "forward", units:
                position += int(units)
                depth += aim * int(units)
            case "down", units:
                aim += int(units)
            case "up", units:
                aim -= int(units)
            case _:
                print("[ERROR] unrecognized command.")

    return position * depth

def main():
    '''Main function'''
    with open("aoc2_input.txt", "r", encoding = "utf-8") as file:
        directions = [d.strip().split() for d in file.readlines()]

    print(task_1(directions))
    print(task_2(directions))

if __name__ == "__main__":
    main()
