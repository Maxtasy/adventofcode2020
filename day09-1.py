#https://adventofcode.com/2020/day/9


PREAMBLE_SIZE = 25


def part1(input_file):
  with open(input_file, "r") as f:
    numbers = list(map(int, f.read().strip().split("\n")))
    
    for i in range(PREAMBLE_SIZE, len(numbers)):
      valid = False
      num_arr = numbers[i - PREAMBLE_SIZE:i]
      for j in range(len(num_arr)):
        for k in range(len(num_arr) - j):
          if num_arr[j] + num_arr[j+k] == numbers[i]:
            valid = True
      
      if not valid:
        return numbers[i]

    
def main():
  input_file = "day09-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()