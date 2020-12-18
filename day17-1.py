#https://adventofcode.com/2020/day/17


from collections import defaultdict
from copy import deepcopy


CYCLES = 6


def active_neighbor_count(hyperplane, coord):
  count = 0
  for z in range(-1, 2):
    for y in range(-1, 2):
      for x in range(-1, 2):
        neighbor_coord = (coord[0]+z, coord[1]+y, coord[2]+x)
        if neighbor_coord != coord and hyperplane[neighbor_coord]:
          count += 1
  
  return count


def part1(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    hyperplane = defaultdict(lambda: False)
    
    current_min_z = 0
    current_max_z = 0
    current_min_y = 0
    current_max_y = 0
    current_min_x = 0
    current_max_x = 0

    for y in range(len(lines)):
      for x in range(len(lines[y])):
        z = 0
        if lines[y][x] == "#":
          hyperplane[(z, y, x)] = True
          current_min_z = min(current_min_z, z)
          current_max_z = max(current_max_z, z)
          current_min_y = min(current_min_y, y)
          current_max_y = max(current_max_y, y)
          current_min_x = min(current_min_x, x)
          current_max_x = max(current_max_x, x)

    for _ in range(CYCLES):
      hyperplane_copy = deepcopy(hyperplane)
      for z in range(current_min_z - 1, current_max_z + 2):
        for y in range(current_min_y - 1, current_max_y + 2):
          for x in range(current_min_x - 1, current_max_x + 2):
            active_neighbors = active_neighbor_count(hyperplane_copy, (z, y, x))

            if hyperplane_copy[(z, y, x)] and not active_neighbors in range(2,4):
              hyperplane[(z, y, x)] = False
            elif not hyperplane_copy[(z, y, x)] and active_neighbors == 3:
              hyperplane[(z, y, x)] = True
              current_min_z = min(current_min_z, z)
              current_max_z = max(current_max_z, z)
              current_min_y = min(current_min_y, y)
              current_max_y = max(current_max_y, y)
              current_min_x = min(current_min_x, x)
              current_max_x = max(current_max_x, x)
    
    active_count = 0
    for coord in hyperplane:
      if hyperplane[coord]:
        active_count += 1
    
    return active_count


def main():
  input_file = "day17-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()