#https://adventofcode.com/2020/day/12


def part2(input_file):
  with open(input_file, "r") as f:
    instructions = f.read().strip().split("\n")

    cur_row = 0
    cur_col = 0

    waypoint_distance_row = 1
    waypoint_distance_col = 10

    for instruction in instructions:
      if instruction[0] == "N":
        waypoint_distance_row += int(instruction[1:])
      elif instruction[0] == "S":
        waypoint_distance_row -= int(instruction[1:])
      elif instruction[0] == "E":
        waypoint_distance_col += int(instruction[1:])
      elif instruction[0] == "W":
        waypoint_distance_col -= int(instruction[1:])
      elif instruction[0] == "R":
        right_rotations = int(instruction[1:]) // 90
        for _ in range(right_rotations):
          temp = waypoint_distance_col
          waypoint_distance_col = waypoint_distance_row
          waypoint_distance_row = -temp
      elif instruction[0] == "L":
        left_rotations = int(instruction[1:]) // 90
        for _ in range(left_rotations):
          temp = waypoint_distance_col
          waypoint_distance_col = -waypoint_distance_row
          waypoint_distance_row = temp
      elif instruction[0] == "F":
        cur_row += int(instruction[1:]) * waypoint_distance_row
        cur_col += int(instruction[1:]) * waypoint_distance_col
    
    return abs(cur_row) + abs(cur_col)

    
def main():
  input_file = "day12-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()