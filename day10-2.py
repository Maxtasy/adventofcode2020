#https://adventofcode.com/2020/day/10


from collections import defaultdict


def part2(input_file):
    with open(input_file, "r") as f:
      jolts = [0]
      highest = 0

      for line in f:
        line = line.strip("\n")
        jolts.append(int(line))
        highest = max(highest, int(line))

      jolts.append(highest + 3)

      jolts = sorted(jolts)

      ways = defaultdict(lambda:0)
      ways[0] = 1


      for i in range(1, len(jolts)):
        ways[jolts[i]] = ways[jolts[i]-1] + ways[jolts[i]-2] + ways[jolts[i]-3]

      return ways[jolts[-1]]

    
def main():
  input_file = "day10-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()