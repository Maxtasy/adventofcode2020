#https://adventofcode.com/2020/day/12


def part1(input_file):
  with open(input_file, "r") as f:
    instructions = f.read().strip().split("\n")

    directions =[(1, 0), (0, 1), (-1, 0), (0, -1)]
    cur_dir = (0, 1)
    cur_row = 0
    cur_col = 0

    for instruction in instructions:
      if instruction[0] == "N":
        cur_row += int(instruction[1:])
      elif instruction[0] == "S":
        cur_row -= int(instruction[1:])
      elif instruction[0] == "E":
        cur_col += int(instruction[1:])
      elif instruction[0] == "W":
        cur_col -= int(instruction[1:])
      elif instruction[0] == "R":
        right_rotations = int(instruction[1:]) // 90
        cur_dir = directions[(directions.index(cur_dir) + right_rotations) % len(directions)]
      elif instruction[0] == "L":
        right_rotations = int(instruction[1:]) // 90
        cur_dir = directions[(directions.index(cur_dir) - right_rotations) % len(directions)]
      elif instruction[0] == "F":
        cur_row += cur_dir[0] * int(instruction[1:])
        cur_col += cur_dir[1] * int(instruction[1:])
    
    return abs(cur_row) + abs(cur_col)

    
def main():
  input_file = "day12-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()