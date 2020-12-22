#https://adventofcode.com/2020/day/20


def part1(input_file):
  with open(input_file, "r") as f:
    tiles_arr = f.read().strip().split("\n\n")

    tiles = {}

    for part in tiles_arr:
      lines = part.split("\n")
      id = int(lines[0].replace(":", "").split(" ")[1])
      tiles[id] = []
      tiles[id].append(lines[1])
      tiles[id].append(lines[-1])
      left = ""
      right = ""
      for i in range(1, len(lines)):
        left += lines[i][0]
        right += lines[i][-1]
        
      tiles[id].append(left)
      tiles[id].append(right)
    
    # look for the 4 corner pieces (they each have 2 sides that don't match any others)
    corner_tiles = []

    for key in tiles.keys():
      matching_tiles = 0

      other_tiles = list(tiles.keys())
      other_tiles.remove(key)

      for side in tiles[key]:
        for tile in other_tiles:
          for i in range(len(tiles[tile])):
            if side == tiles[tile][i] or side == tiles[tile][i][::-1]:
              matching_tiles += 1
      
      if matching_tiles < 3:
        corner_tiles.append(key)
    
    result = 1
    for corner_tile in corner_tiles:
      result *= corner_tile
    
    return result


def main():
  input_file = "day20-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()