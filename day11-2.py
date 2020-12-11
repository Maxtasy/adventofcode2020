#https://adventofcode.com/2020/day/11


from copy import deepcopy


def part2(input_file):
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

          #up
          for i in range(row, -1, -1):
            if i == row:
              continue
            if seat_states_copy[i][col] == False:
              break
            if seat_states_copy[i][col] == True:
              surrounding_occupied_seats += 1
              break
          #down
          for i in range(row, grid_rows):
            if i == row:
              continue
            if seat_states_copy[i][col] == False:
              break
            if seat_states_copy[i][col] == True:
              surrounding_occupied_seats += 1
              break
          #left
          for i in range(col, -1, -1):
            if i == col:
              continue
            if seat_states_copy[row][i] == False:
              break
            if seat_states_copy[row][i] == True:
              surrounding_occupied_seats += 1
              break
          #right
          for i in range(col, grid_cols):
            if i == col:
              continue
            if seat_states_copy[row][i] == False:
              break
            if seat_states_copy[row][i] == True:
              surrounding_occupied_seats += 1
              break
          #diag up left
          for i in range(1, grid_cols):
            if row - i < 0 or col - i < 0:
              break
            if seat_states_copy[row - i][col - i] == False:
              break
            if seat_states_copy[row - i][col - i] == True:
              surrounding_occupied_seats += 1
              break
          #diag up right
          for i in range(1, grid_cols):
            if row - i < 0 or col + i >= grid_cols:
              break
            if seat_states_copy[row - i][col + i] == False:
              break
            if seat_states_copy[row - i][col + i] == True:
              surrounding_occupied_seats += 1
              break
          #diag down right
          for i in range(1, grid_cols):
            if row + i >= grid_rows or col + i >= grid_cols:
              break
            if seat_states_copy[row + i][col + i] == False:
              break
            if seat_states_copy[row + i][col + i] == True:
              surrounding_occupied_seats += 1
              break
          #diag down left
          for i in range(1, grid_cols):
            if row + i >= grid_rows or col - i < 0:
              break
            if seat_states_copy[row + i][col - i] == False:
              break
            if seat_states_copy[row + i][col - i] == True:
              surrounding_occupied_seats += 1
              break

          if seat_states_copy[row][col] == True:
            if surrounding_occupied_seats >= 5:
              seat_states[row][col] = False
          elif seat_states_copy[row][col] == False:
            if surrounding_occupied_seats == 0:
              seat_states[row][col] = True
    
      occupied_seats = 0

      for row in range(grid_rows):
        for col in range(grid_cols):
          if seat_states[row][col]:
            occupied_seats += 1

      if seat_states == seat_states_copy:
        break
    
    return occupied_seats

    
def main():
  input_file = "day11-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()