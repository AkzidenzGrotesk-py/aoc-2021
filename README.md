# Advent of Code 2021
![akzidenz 50*](https://github.com/AkzidenzGrotesk-py/AkzidenzGrotesk-py.github.io/blob/main/resources/success.PNG?raw=true)

My Python solutions to AoC 2021 problems.

Maybe a mess. Not really competitive. I have main() though.

My own personal modules `termbars` and `my_helper` are present in some of the solutions. 
Those are found in the [PythonProjects/misc/modules/](https://github.com/AkzidenzGrotesk-py/PythonProjects/tree/main/misc/modules) folder. I will most likely add more utility functions for next year.

<details>
  <summary>Code format for most of the puzzles.</summary>

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
  
</details>
