'''Advent of code, day 21: DIRAC DICE'''
from copy import deepcopy

DETER_DICE = 0
TOTAL_DIE_ROLLS = 0
BELL_ROLL = [
    # roll, chance (bell curve!)
    [3, 1],
    [4, 3],
    [5, 6],
    [6, 7],
    [7, 6],
    [8, 3],
    [9, 1]
]

def roll_deter():
    global DETER_DICE, TOTAL_DIE_ROLLS
    DETER_DICE += 1
    if DETER_DICE == 101:
        DETER_DICE = 1

    TOTAL_DIE_ROLLS += 1
    return DETER_DICE

def task_1(starting):
    '''Code for task 1:
    '''
    turn = False
    positions = deepcopy(starting)
    points = [0 for _ in starting]
    print(positions)
    while 1:
        roll = [roll_deter() for _ in range(3)]
        positions[int(turn)] += sum(roll)
        pnts = int(str(positions[int(turn)])[-1])
        points[int(turn)] += pnts if pnts != 0 else 10
        print(f"Player {int(turn)+1} rolled {roll} -> {sum(roll)}. Their new position is {positions[int(turn)]}, and new points is {points[int(turn)]}")

        if points[int(turn)] >= 1000:
            print(TOTAL_DIE_ROLLS)
            return points[int(not turn)] * TOTAL_DIE_ROLLS

        turn = not turn


def task_2(starting):
    '''Code for task 2:
    '''
    def recur_posb(scA, scB, psA, psB):
        '''Recur through possibilities'''
        win, lose = 0, 0
        for roll, chance in BELL_ROLL:
            newpos = int(str(psA + roll)[-1])
            newpos = newpos if newpos != 0 else 10
            nlo, nwm = (0, 1) if scA + newpos >= 21 else recur_posb(scB, scA + newpos, psB, newpos)
            win += nwm * chance
            lose += nlo * chance
        return win, lose

    return recur_posb(0, 0, starting[0], starting[1])


def main():
    '''Main function'''
    with open("aoc21_input.txt", "r", encoding = "utf-8") as file:
        contents = file.readlines()
        player_starts = [int(contents[0][27:]), int(contents[1][27:])]

    print(task_1(player_starts))
    print(task_2(player_starts))

if __name__ == "__main__":
    main()
