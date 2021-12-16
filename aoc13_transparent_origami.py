'''Advent of code, day 13: TRANSPARENT ORIGAMI'''
from os import system

def fold_point_horz(point, fold_x):
    '''Fold a point'''
    if point[0] < fold_x:
        return point
    if point[0] == fold_x:
        return None

    point_dist = point[0] - fold_x
    return [abs(fold_x - point_dist), point[1]]

def fold_point_vert(point, fold_y):
    '''Fold a point'''
    if point[1] < fold_y:
        return point
    if point[1] == fold_y:
        return None

    point_dist = point[1] - fold_y
    return [point[0], abs(fold_y - point_dist)]


def task_1(points, folds):
    '''Code for task 1:
    '''
    new_points = []
    for point in points:
        folded = fold_point_horz(point, folds[0][1])
        if folded not in new_points and folded:
            new_points.append(folded)

    return len(new_points)

def task_2(points, folds):
    '''Code for task 2:
    '''
    for fold in folds:
        new_points = []
        for point in points:
            folded = fold_point_horz(point, fold[1])\
                if fold[0] == 'x' else fold_point_vert(point, fold[1])
            if folded not in new_points and folded:
                new_points.append(folded)
        points = new_points

    system("cls")
    for point in points:
        print(f"\033[{point[1]};{point[0]}H#", end='')
    print("\033[7;0H",end="")

def main():
    '''Main function'''
    with open("aoc13_input.txt", "r", encoding = "utf-8") as file:
        contents = file.readlines()

        points = []
        folds = []
        current = False
        for line in contents:
            if line == "\n":
                current = not current
                continue
            if not current:
                points.append([int(i) for i in line.split(",")])
            if current:
                fold = line.split()[2]
                fold = fold.split("=")
                folds.append([fold[0], int(fold[1])])

    print(task_1(points, folds))
    print(task_2(points, folds))

if __name__ == "__main__":
    main()
