#https://adventofcode.com/2020/day/1


def part2(input_file):
  with open(input_file, "r") as f:
    input_str = f.read().strip()
    number_array = list(map(int, input_str.split("\n")))
    for i in range(len(number_array)):
      for j in range(len(number_array) - 1 - i):
        for k in range(len(number_array) - 1 - i - j):
          result = number_array[i] + number_array[i+j+1] + number_array[i+k+1]
          if result == 2020:
            return number_array[i] * number_array[i+j+1] * number_array[i+k+1]


def main():
  input_file = "day01-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()