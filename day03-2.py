#https://adventofcode.com/2020/day/3


def part2(input_file):
  with open(input_file, "r") as f:
    grid = f.read().strip().split("\n")

    slopes = [
      {"x": 1, "y": 1},
      {"x": 3, "y": 1},
      {"x": 5, "y": 1},
      {"x": 7, "y": 1},
      {"x": 1, "y": 2}
    ]

    product = 1

    for slope in slopes:
      current_pos = {"x": 0, "y": 0}
      tree_count = 0
      for i in range(0, len(grid), slope["y"]):
        if grid[i][current_pos["x"]] == "#":
          tree_count += 1
        
        current_pos["x"] = (current_pos["x"] + slope["x"]) % len(grid[0])
      
      product *= tree_count
  
  return product


def main():
  input_file = "day03-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()