'''Advent of code, day 5: HYDROTHERMAL VENTURE'''
from pprint import pprint
from collections import Counter

def point2_to_vhline(point1, point2) -> list[tuple]:
    '''Converts 2 points into a vert/horz line'''
    ind = int(point1[0] == point2[0])
    gen_start = point1[ind] if point1[ind] < point2[ind] else point2[ind]
    gen_end = point1[ind] if gen_start == point2[ind] else point2[ind]
    gradient = [
        (point1[0] if ind else x, point1[1] if not ind else x)
        for x in range(gen_start + 1, gen_end)
    ]
    return [tuple(point1), *gradient, tuple(point2)]

def expand_and_count(line_pairs) -> int:
    '''Expands sublists and counts # of duplicate values'''
    line_pairs = Counter([item for sublist in line_pairs for item in sublist])
    line_pairs = [pair for pair in line_pairs if line_pairs[pair] > 1]
    line_pairs = list(set(line_pairs))

    return len(line_pairs)


def task_1(line_pairs):
    '''Code for task 1:
    For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.
    Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
    '''
    # Filter out non-straight lines
    line_pairs = list(filter(lambda e: e[0][0] == e[1][0] or e[0][1] == e[1][1], line_pairs))

    for pair_number, pair in enumerate(line_pairs):
        line_pairs[pair_number] = point2_to_vhline(pair[0], pair[1])
    return expand_and_count(line_pairs)

def task_2(line_pairs):
    '''Code for task 2:
    You still need to determine the number of points where at least two lines overlap.
    Consider all of the lines. At how many points do at least two lines overlap?
    '''
    for pair_number, pair in enumerate(line_pairs):
        point1 = pair[0]
        point2 = pair[1]

        if point1[0] == point2[0] or point1[1] == point2[1]:
            line_pairs[pair_number] = point2_to_vhline(point1, point2)
        else:
            # Generate gradients from x1 -> x2 and y1 -> y2 and merge
            gradients = []
            for ind in range(2):
                gen_start = point1[ind] if point1[ind] < point2[ind] else point2[ind]
                gen_end = point1[ind] if gen_start == point2[ind] else point2[ind]
                gradients.append(list(range(gen_start + 1, gen_end)))
                if gen_start == point2[ind]:
                    gradients[-1].reverse()

            gradient = [(gradients[0][i], gradients[1][i]) for i, _ in enumerate(gradients[0])]
            line_pairs[pair_number] = [tuple(point1), *gradient, tuple(point2)]

    return expand_and_count(line_pairs)

def main():
    '''Main function'''
    with open("aoc5_input.txt", "r", encoding = "utf-8") as file:
        contents = file.readlines()

        # Convert data in form "x,y -> x,y"
        all_points = []
        for line in contents:
            point_sets = line.strip().split(" -> ")
            this_point_set = []
            for points in point_sets:
                split_points = points.split(",")
                this_point_set.append([int(split_points[0]), int(split_points[1])])
            all_points.append(this_point_set)


    print(task_1(all_points))
    print(task_2(all_points))

if __name__ == "__main__":
    main()
