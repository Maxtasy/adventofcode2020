#https://adventofcode.com/2020/day/3


def part1(input_file):
  with open(input_file, "r") as f:
    grid = f.read().strip().split("\n")
    slope = {"x": 3, "y": 1}
    current_x = 0
    tree_count = 0
    for row in grid:
      if row[current_x] == "#":
        tree_count += 1
      
      current_x = (current_x + slope["x"]) % len(grid[0])
  
  return tree_count


def main():
  input_file = "day03-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()