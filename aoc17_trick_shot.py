'''Advent of code, day 17: TRICK SHOT'''
from math import inf
from termbars import TerminalBar, TBPRESET_MODERN

class Probe:
    '''Probe class'''
    def __init__(self, velx, vely):
        self.vel = [velx, vely]
        self.pos = [0, 0]
        self.highest_y = -inf

    def step(self):
        '''Perform step'''
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.highest_y = self.pos[1] if self.pos[1] > self.highest_y else self.highest_y
        self.vel[0] += -1 if self.vel[0] > 0 else (1 if self.vel[0] < 0 else 0)
        self.vel[1] -= 1

    def in_target(self, target: list[list[int, int], list[int, int]]):
        '''Check if in the target zone'''
        return target[0][0] <= self.pos[0] <= target[0][1] \
            and target[1][0] <= self.pos[1] <= target[1][1]

    def past_target(self, target: list[list[int, int], list[int, int]]):
        '''Check if past the target'''
        return self.pos[0] > target[0][1] \
            or self.pos[1] < target[1][0] \
            or (self.vel[0] == 0 and not target[0][0] <= self.pos[0] <= target[0][1])

def simulate_probes(target_area, lowx = 1, lowy = 1, limitx = 500, limity = 500):
    '''Simulate probes'''
    tbar = TerminalBar((limitx-lowx) * (limity-lowy))
    tbar.update_preset(TBPRESET_MODERN)
    highest_height = [-inf, 0, 0]
    number_of_successes = 0
    for velx in range(lowx, limitx):
        for vely in range(lowy, limity):
            tbar.update(tbar.bar_state[0] + 1)
            probe = Probe(velx, vely)
            while not probe.past_target(target_area):
                probe.step()
                if probe.in_target(target_area):
                    number_of_successes += 1
                    if probe.highest_y > highest_height[0]:
                        highest_height = [probe.highest_y, velx, vely]
                    break

    return highest_height, number_of_successes


def task_1(simul):
    '''Code for task 1:
    '''
    return simul[0]

def task_2(simul):
    '''Code for task 2:
    '''
    return simul[1]

def main():
    '''Main function'''
    with open("aoc17_input.txt", "r", encoding = "utf-8") as file:
        contents = file.readlines()
        target_area = contents[0].split("=")
        target_area = [target_area[1].split(".."), target_area[2].split("..")]
        target_area = [[int(target_area[0][0]), int(target_area[0][1][:-3])],
                       [int(target_area[1][0]), int(target_area[1][1])]]
    simul_probes = simulate_probes(target_area, -500, -500, 500, 500)
    print(task_1(simul_probes))
    print(task_2(simul_probes))

if __name__ == "__main__":
    main()
