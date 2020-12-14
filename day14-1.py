#https://adventofcode.com/2020/day/14


from collections import defaultdict


def part1(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    addresses = defaultdict(int)
    mask = ["X" for i in range(36)]

    for line in lines:
      line_parts = line.split(" = ")
      if line_parts[0] == "mask":
        mask = line_parts[1]
      else:
        address = int(line_parts[0][4:-1])
        number = int(line_parts[1])
        number_bin_arr = list("{0:b}".format(number).rjust(36, "0"))
        for i in range(len(mask)):
          if mask[i] == "X":
            continue
          else:
            number_bin_arr[i] = mask[i]
        number = int("".join(number_bin_arr), 2)
        addresses[address] = number
    
    return sum(addresses.values())

    
def main():
  input_file = "day14-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()