'''Advent of code, day 19: BEACON SCANNER'''
from math import inf

ORDERS = [
    [0, 1, 2],
    [0, 2, 1],
    [1, 0, 2],
    [1, 2, 0],
    [2, 1, 0],
    [2, 0, 1],
]
NEGATIVITIES = [
    [1, 1, 1],
    [1, -1, 1],
    [1, 1, -1],
    [1, -1, -1],
    [-1, 1, 1],
    [-1, -1, 1],
    [-1, 1, -1],
    [-1, -1, -1],
]

def reorder(order, negativity, scan):
    '''Remap scans [(x, y, z), (...)] to order and with negativity'''
    return [
        [negativity[0] * item[order[0]],
        negativity[1] * item[order[1]],
        negativity[2] * item[order[2]]
        ] for item in scan
    ]

distances_from_scan_0 = [(0, 0, 0)]
def find_alignments(scan_a, scan_b):
    '''Find alignments between two scanners'''
    in_a = {tuple(x) for x in scan_a}

    for remap in ORDERS:
        for negatives in NEGATIVITIES:
            mod_scan_b = reorder(remap, negatives, scan_b)
            for a_pos in scan_a:
                for b_pos in mod_scan_b:
                    remaps = [b_pos[i] - a_pos[i] for i in range(3)]
                    matches = 0
                    all_remapped = []
                    for other_b in mod_scan_b:
                        remapped_to_a = tuple(other_b[i] - remaps[i] for i in range(3))
                        if remapped_to_a in in_a:
                            matches += 1
                        all_remapped.append(list(remapped_to_a))
                    if matches >= 12:
                        distances_from_scan_0.append(tuple(remaps))
                        return (True, all_remapped)
    return (False, None)

def task_1(beacons):
    '''Code for task 1:
    '''
    aligned_indices = set([0])
    aligned = {}
    aligned[0] = beacons[0]
    all_aligned = []
    all_aligned += [tuple(x) for x in beacons[0]]
    noalign = set()
    while len(aligned_indices) < len(beacons):
        for i, _ in enumerate(beacons):
            if i in aligned_indices:
                continue
            for j in aligned_indices:
                print(f"Checking {i} = {j}")
                if (i, j) in noalign:
                    continue
                has_enough_alignments, remap = find_alignments(aligned[j], beacons[i])
                if has_enough_alignments:
                    aligned_indices.add(i)
                    aligned[i] = remap
                    all_aligned += [tuple(x) for x in remap]
                    break
                noalign.add((i, j))

    return len(set(all_aligned))

def task_2(beacons):
    '''Code for task 2:
    '''
    max_val = -inf
    for i, a_check in enumerate(distances_from_scan_0):
        for j, b_check in enumerate(distances_from_scan_0):
            if i == j:
                continue
            manhattan = sum([abs(a_check[0] - b_check[0]),\
                    abs(a_check[1] - b_check[1]),\
                    abs(a_check[2] - b_check[2])])
            if manhattan > max_val:
                max_val = manhattan
    return max_val

def main():
    '''Main function'''
    with open("aoc19_input.txt", "r", encoding = "utf-8") as file:
        contents = file.read().split("\n\n")
        beacons = [
            [
                [int(i) for i in l.split(",")]
                for l in line.split("\n")[1:]
            ] for line in contents
        ]
    print(task_1(beacons))
    print(task_2(beacons))

if __name__ == "__main__":
    main()
