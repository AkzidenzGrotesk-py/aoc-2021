'''Advent of code, day 20: TRENCH MAP'''
from my_helper import DIRS_3x3, generate_around

def margin(inp_mat: list[list], value: int = 0) -> list[list]:
    ygen = [value for i in inp_mat[0]]
    inp_mat = [ygen, *inp_mat, ygen]
    return [[value, *line, value] for line in inp_mat]

def task_1(algo, image, times = 2):
    '''Code for task 1:
    '''
    switch = 0
    for i in range(times):
        print(f"Computing {i+1}th iteration...")
        image = margin(image, switch)
        new_image = [[0 for _ in line] for line in image]
        image = margin(image, switch)
        switch = algo[0] if not switch else algo[511]
        image = [
            [
                algo[int("".join([
                        str(image[iy][ix])
                        for ix, iy in generate_around(x+1, y+1, len(image[0]), len(image), DIRS_3x3)
                ]), 2)] for x in range(len(new_image[0]))
            ] for y in range(len(new_image))
        ]
        image = new_image

    return sum([sum(i) for i in image])


def task_2(algo, image):
    '''Code for task 2:
    '''
    return task_1(algo, image, 50)

def main():
    '''Main function'''
    with open("aoc20_input.txt", "r", encoding = "utf-8") as file:
        contents = file.read().split("\n\n")
        algo = [0 if c == '.' else 1 for c in contents[0].strip()]
        image = [
            [0 if c == '.' else 1
            for c in line.strip()]
            for line in contents[1].split("\n")
        ]

    print(task_1(algo, image))
    print(task_2(algo, image))

if __name__ == "__main__":
    main()
