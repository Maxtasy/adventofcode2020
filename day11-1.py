#https://adventofcode.com/2020/day/11


from copy import deepcopy


def part1(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    grid_rows = len(lines)
    grid_cols = len(lines[0])
    
    seat_states = []

    for i in range(len(lines)):
      row = []

      for char in lines[i]:
        if char == "#":
          row.append(True)
        elif char == "L":
          row.append(False)
        else:
          row.append(None)
      
      seat_states.append(row)

    while True:
      seat_states_copy = deepcopy(seat_states)
      for row in range(grid_rows):
        for col in range(grid_cols):
          surrounding_occupied_seats = 0

          for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
              if row_offset == 0 and col_offset == 0:
                continue

              n_row = row + row_offset
              n_col = col + col_offset

              if (n_row < 0) or (n_row >= grid_rows) or (n_col < 0) or (n_col >= grid_cols):
                continue

              if seat_states_copy[n_row][n_col]:
                surrounding_occupied_seats += 1
          
          if seat_states_copy[row][col] == True:
            if surrounding_occupied_seats >= 4:
              seat_states[row][col] = False
          elif seat_states_copy[row][col] == False:
            if surrounding_occupied_seats == 0:
              seat_states[row][col] = True
      
      if seat_states == seat_states_copy:
        break
    
    occupied_seats = 0

    for row in range(grid_rows):
      for col in range(grid_cols):
        if seat_states[row][col]:
          occupied_seats += 1
    
    return occupied_seats

    
def main():
  input_file = "day11-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()