'''Advent of code, day 4: GIANT SQUID'''
# from pprint import pprint

def contains_bingo(board) -> bool:
    '''Checks if a board contains a BINGO!'''
    for row in board:
        if "".join(row) == "XXXXX":
            return True

    for column in [
        [bit[row] for bit in board]
        for row, _ in enumerate(board[0])
    ]:
        if "".join(column) == "XXXXX":
            return True

    return False

def score_bingo_board(board, win_num) -> int:
    '''Gives score to bingo board'''
    nums = [
        sum([int(cell) for cell in line if cell != "X"])
        for line in board if "".join(line) != "XXXXX"
    ]

    return sum(nums) * int(win_num)


def task_1(bingo_nums, bingo_boards):
    '''Code for task 1:
    The submarine has a bingo subsystem to help passengers
    (currently, you and the giant squid) pass the time.
    It automatically generates a random order in which to draw
    numbers and a random set of boards (your puzzle input).
    The score of the winning board can now be calculated.
    Start by finding the sum of all unmarked numbers on that board;
    in this case, the sum is 188. Then, multiply that sum by the
    number that was just called when the board won, 24, to get the
    final score, 188 * 24 = 4512.
    To guarantee victory against the giant squid,
    figure out which board will win first.
    What will your final score be if you choose that board?
    '''

    bingo_found = False
    bingo_board = None
    bingo_win_num = None
    for num in bingo_nums:
        for brd_n, board in enumerate(bingo_boards):
            for row_n, row in enumerate(board):
                if num in row:
                    bingo_boards[brd_n][row_n][bingo_boards[brd_n][row_n].index(num)] = "X"

            if contains_bingo(board):
                bingo_found = True
                bingo_board = board
                bingo_win_num = num
                break

        if bingo_found:
            break

    return score_bingo_board(bingo_board, bingo_win_num)

def task_2(bingo_nums, bingo_boards):
    '''Code for task 2:
    On the other hand, it might be wise to try a different strategy: let the giant squid win.
    Figure out which board will win last.
    Once it wins, what would its final score be?
    '''
    final_score = None
    for num in bingo_nums:
        for brd_n, board in enumerate(bingo_boards):
            for row_n, row in enumerate(board):
                if num in row:
                    bingo_boards[brd_n][row_n][bingo_boards[brd_n][row_n].index(num)] = "X"

        if len(bingo_boards) == 1:
            if contains_bingo(bingo_boards[0]):
                final_score = score_bingo_board(bingo_boards[0], num)
                break

        bingo_boards[:] = [x for x in bingo_boards if not contains_bingo(x)]

    return final_score

def main():
    '''Main function'''
    with open("aoc4_input.txt", "r", encoding = "utf-8") as file:
        contents = file.readlines()

        # Bingo numbers to be called
        bingo_nums = contents[0].strip().split(",")

        # Bingo boards
        collector = 0
        bingo_boards = []
        for line in contents[2:]:
            if collector >= 0:
                if not collector:
                    bingo_boards.append([])

                bingo_boards[-1].append(line.split())

            collector += 1
            if collector >= 5:
                collector = -1

    print(task_1(bingo_nums, bingo_boards))
    print(task_2(bingo_nums, bingo_boards))

if __name__ == "__main__":
    main()
