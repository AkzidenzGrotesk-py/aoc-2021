'''Advent of code, day 1: SONAR SWEEP'''

def task_1(nums):
    '''Code for task 1:
    Count the number of times a depth measurement increases from the previous measurement.
    How many sums are larger than the previous sum?'''
    return sum([1 for i, _ in enumerate(nums) if nums[i] > nums[i-1]])

def task_2(nums):
    '''Code for task 2:
    Your goal now is to count the number of times the sum of measurements
    in this sliding window increases from the previous sum.
    Consider sums of a three-measurement sliding window.
    How many sums are larger than the previous sum?'''
    # counts the first set as being greater when it should not be counted
    return sum(1 for i, _ in enumerate(nums[:-2]) if sum(nums[i:i+3]) > sum(nums[i-1:i+2])) - 1

def main():
    '''Main function'''
    with open("aoc1_input.txt", "r", encoding = "utf-8") as file:
        nums = [int(n) for n in file.readlines()]

    print(task_1(nums))
    print(task_2(nums))

if __name__ == "__main__":
    main()
