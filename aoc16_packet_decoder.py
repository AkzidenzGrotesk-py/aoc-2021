'''Advent of code, day 16: PACKET DECODER'''
from math import prod

VERSION_TOTAL = 0

def extract_packets(code, cursor = 0, has_padding = True):
    '''Extract packets'''
    global VERSION_TOTAL
    if cursor >= len(code):
        return cursor, None
    version = int(code[cursor:cursor+3], 2)
    cursor += 3
    ptype = int(code[cursor:cursor+3], 2)
    cursor += 3
    VERSION_TOTAL += version
    if ptype == 4:
        collect = ""
        while 1:
            if code[cursor] == "1":
                collect += code[cursor+1:cursor+5]
                cursor += 5
            elif code[cursor] == "0":
                collect += code[cursor+1:cursor+5]
                cursor += 5
                break
        if has_padding:
            cursor += 4 - (cursor % 4)
        while code[cursor:cursor+4] == "0000" and has_padding:
            cursor += 4
        return cursor, int(collect, 2)

    length_type = code[cursor:cursor+1]
    cursor += 1
    if length_type == "0":
        tot_length = int(code[cursor:cursor+15], 2)
        cursor += 15
        cur_cursor = int(cursor)
        sub_packets = []
        while cur_cursor + tot_length > cursor:
            cursor, packet = extract_packets(code, cursor, False)
            if packet is None:
                break
            sub_packets.append(packet)
        if has_padding:
            cursor += 4 - (cursor % 4)
        while code[cursor:cursor+4] == "0000" and has_padding:
            cursor += 4
    elif length_type == "1":
        tot_sub_packets = int(code[cursor:cursor+11], 2)
        cursor += 11
        sub_packets = []
        for _ in range(tot_sub_packets):
            cursor, packet = extract_packets(code, cursor, False)
            if packet is None:
                break
            sub_packets.append(packet)
        if has_padding:
            cursor += 4 - (cursor % 4)
        while code[cursor:cursor+4] == "0000" and has_padding:
            cursor += 4
    match ptype:
        case 0:
            return cursor, sum(sub_packets)
        case 1:
            return cursor, prod(sub_packets)
        case 2:
            return cursor, min(sub_packets)
        case 3:
            return cursor, max(sub_packets)
        case 5:
            return cursor, 1 if sub_packets[0] > sub_packets[1] else 0
        case 6:
            return cursor, 1 if sub_packets[0] < sub_packets[1] else 0
        case 7:
            return cursor, 1 if sub_packets[0] == sub_packets[1] else 0


def task_1(_):
    '''Code for task 1:
    '''
    return VERSION_TOTAL

def task_2(extracted):
    '''Code for task 2:
    '''
    return extracted[1]

def main():
    '''Main function'''
    with open("aoc16_input.txt", "r", encoding = "utf-8") as file:
        contents = file.readlines()
        code = bin(int(contents[0].strip(), 16))[2:].zfill(len(contents[0].strip()) * 4)
    extracted = extract_packets(code)
    print(task_1(extracted))
    print(task_2(extracted))

if __name__ == "__main__":
    main()
