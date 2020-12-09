#https://adventofcode.com/2020/day/9


PREAMBLE_SIZE = 25


def part2(input_file):
  with open(input_file, "r") as f:
    numbers = list(map(int, f.read().strip().split("\n")))
    invalid_number = None
    
    for i in range(PREAMBLE_SIZE, len(numbers)):
      valid = False
      num_arr = numbers[i - PREAMBLE_SIZE:i]
      for j in range(len(num_arr)):
        for k in range(len(num_arr) - j):
          if num_arr[j] + num_arr[j+k] == numbers[i]:
            valid = True
      
      if not valid:
        invalid_number = numbers[i]
        break
    
    for i in range(len(numbers)):
      num_sum = 0
      index = 0
      used_numbers = []
      while num_sum < invalid_number:
        num_sum += numbers[i+index]
        used_numbers.append(numbers[i+index])
        if num_sum == invalid_number:
          return min(used_numbers) + max(used_numbers)
        index += 1

    
def main():
  input_file = "day09-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()