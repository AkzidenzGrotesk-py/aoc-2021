'''Advent of code, day 3: BINARY DIAGNOSTIC'''

def task_1(binary_nums):
    '''Code for task 1:
    Each bit in the gamma rate can be determined by finding the most
    common bit in the corresponding position of all numbers in the diagnostic report.
    Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate,
    then multiply them together. What is the power consumption of the submarine?
    '''

    # Line up binary nums vertically
    rows = [
        "".join([bit[column] for bit in binary_nums])
        for column, _ in enumerate(binary_nums[0])
    ]

    # Generate gamma by checking each vertical row (haha) and placing bit based on #
    gamma = "".join([
        "1" if row.count("1") > row.count("0") else "0"
        for row in rows
    ])

    # Generate epsilon by flipping gamma
    epsilon = "".join(["1" if g == "0" else "0" for g in gamma])

    return int(gamma, 2) * int(epsilon, 2)

def task_2(binary_nums):
    '''Code for task 2:
    - Keep only numbers selected by the bit criteria for
    the type of rating value for which you are searching.
    Discard numbers which do not match the bit criteria.
    - If you only have one number left, stop; this is the rating value for which you are searching.
    - Otherwise, repeat the process, considering the next bit to the right.

    The bit criteria depends on which type of rating value you want to find:
    - To find oxygen generator rating, determine the most common value (0 or 1) in the
    current bit position, and keep only numbers with that bit in that position.
    If 0 and 1 are equally common, keep values with a 1 in the position being considered.
    - To find CO2 scrubber rating, determine the least common value (0 or 1) in the current
    bit position, and keep only numbers with that bit in that position. If 0 and 1 are
    equally common, keep values with a 0 in the position being considered.
    Use the binary numbers in your diagnostic report to calculate the oxygen generator
    rating and CO2 scrubber rating, then multiply them together. What is the life support
    rating of the submarine?
    '''

    oxy_binn, co2_binn = binary_nums.copy(), binary_nums.copy()

    for column, _ in enumerate(oxy_binn[0]):
        # Generate column and choose which has less, filter out all numbers which do not contain that bit in said column
        if len(oxy_binn) > 1:
            fcolumn_oxy = "".join([bit[column] for bit in oxy_binn])
            throw_oxy = "1" if fcolumn_oxy.count("1") < fcolumn_oxy.count("0") else "0"
            oxy_binn = list(filter(lambda e: e[column] != throw_oxy, oxy_binn))

        if len(co2_binn) > 1:
            fcolumn_co2 = "".join([bit[column] for bit in co2_binn])
            throw_co2 = "0" if fcolumn_co2.count("1") < fcolumn_co2.count("0") else "1"
            co2_binn = list(filter(lambda e: e[column] != throw_co2, co2_binn))

        if len(co2_binn) == 1 and len(oxy_binn) == 1:
            break

    return int(oxy_binn[0], 2) * int(co2_binn[0], 2)

def main():
    '''Main function'''
    with open("aoc3_input.txt", "r", encoding = "utf-8") as file:
        binary_nums = [l.strip() for l in file.readlines()]


    # print(binary_nums)
    print(task_1(binary_nums))
    print(task_2(binary_nums))

if __name__ == "__main__":
    main()
