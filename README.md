# Advent of Code 2021
My Python solutions to AOC 2021 problems.

Maybe a mess. Not really competitive. I have main() though.

## In format:
```py
'''Advent of code, day X: TITLE'''

def task1(INPUT):
  '''Code for task 1:
  DESCRIPTION
  '''
  ...
  return VALUE

def task2(INPUT):
  '''Code for task 2:
  DESCRIPTION
  '''
  ...
  return VALUE
  
def main():
  '''Main function'''
  with open("aocX_input.txt", "r", encoding = "utf-8") as file:
    CONVERT INTO INPUT
    
  print(task_1(INPUT))
  print(task_2(INPUT))
  
if __name__ == "__main__":
  main()
```
