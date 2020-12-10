#https://adventofcode.com/2020/day/10


def part1(input_file):
  with open(input_file, "r") as f:
    adapters = sorted(list(map(int, f.read().strip().split("\n"))))
    
    device_joltage_rating = max(adapters) + 3

    adapters.append(device_joltage_rating)

    current_jolts = 0
    one_jolt_diffs = 0
    three_jolt_diffs = 0

    for i in range(len(adapters)):
      diff = adapters[i] - current_jolts
      if diff == 1:
        one_jolt_diffs += 1
      elif diff == 3:
        three_jolt_diffs += 1
      
      current_jolts = adapters[i]
    

    return one_jolt_diffs * three_jolt_diffs

    
def main():
  input_file = "day10-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()