'''Advent of code, day 8: SEVEN SEGMENT SEARCH'''

def match_two_str(string1, string2) -> int:
    total = 0
    for ch in string1:
        if ch in string2:
            total += 1
    return total


def task_1(segments):
    '''Code for task 1:
    '''

    total = sum([
        sum([
            1 for elem in line[1] if len(elem) in [2, 3, 7, 4]
        ]) for line in segments
    ])

    return total

def task_2(segments):
    '''Code for task 2:
    '''

    total = 0
    for line in segments:
        # place guaranteed values (1, 4, 7, 8) at front of list
        new_segment = []
        for number in line[0]:
            if len(number) in [2, 3, 4, 7]:
                new_segment.append(number)
        new_segment.extend(list(filter(lambda e: e not in new_segment, line[0])))
        line[0] = new_segment
        values = { i : "" for i in range(10) }

        # create case for every number
        for number in line[0]:
            match len(number):
                case 2:
                    values[1] = number
                case 3:
                    values[7] = number
                case 7:
                    values[8] = number
                case 4:
                    values[4] = number
                case 6:
                    if match_two_str(number, values[1]) == 1:
                        values[6] = number
                    else:
                        if match_two_str(number, values[4]) == 4:
                            values[9] = number
                        else:
                            values[0] = number
                case 5:
                    if match_two_str(number, values[4]) == 2:
                        values[2] = number
                    else:
                        if match_two_str(number, values[1]) == 2:
                            values[3] = number
                        else:
                            values[5] = number

        total += int("".join([
            "".join([
                str(value) for value in values
                if len(number) == match_two_str(number, values[value])
                and len(number) == len(values[value])
            ]) for number in line[1]
        ]))

    return total

def main():
    '''Main function'''
    with open("aoc8_input.txt", "r", encoding = "utf-8") as file:
        contents = file.readlines()

        # Convert data in form "a b c d e f g h i j | k l m n o"
        segments = []
        for line in contents:
            segments.append([])
            sides = line.split("|")
            segments[-1].append([])
            for one in sides[0].split():
                segments[-1][0].append(one.strip())
            segments[-1].append([])
            for four in sides[1].split():
                segments[-1][1].append(four.strip())

    print(task_1(segments))
    print(task_2(segments))

if __name__ == "__main__":
    main()
