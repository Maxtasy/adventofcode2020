#https://adventofcode.com/2020/day/15


from collections import defaultdict


def part1(input_file):
  with open(input_file, "r") as f:
    lines = list(map(int, f.read().strip().split(",")))

    number_indexes = defaultdict(list)
    last_number = None
    current_turn = 1

    for number in lines:
      number_indexes[number].append(current_turn)
      last_number = number
      current_turn += 1

    while current_turn <= 2020:
      # if last number was spoken less than 2 times 
      # number of current index will be 0
      if len(number_indexes[last_number]) < 2:
        number = 0
      else:
        number = number_indexes[last_number][1] - number_indexes[last_number][0]
      
      number_indexes[number].append(current_turn)
      if len(number_indexes[number]) > 2:
        number_indexes[number] = number_indexes[number][1:]
      
      last_number = number

      current_turn += 1

    return last_number

    
def main():
  input_file = "day15-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()