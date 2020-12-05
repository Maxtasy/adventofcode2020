#https://adventofcode.com/2020/day/5


def part2(input_file):
  with open(input_file, "r") as f:
    boarding_passes = f.read().strip().split("\n")
    seat_ids = []

    for boarding_pass in boarding_passes:
      row_min = 0
      row_max = 127
      col_min = 0
      col_max = 7

      for instr in boarding_pass:
        if row_max == row_min and col_max == col_min:
          break
        elif instr == "F":
          row_max = (row_min + row_max - 1) // 2
        elif instr == "B":
          row_min = (row_min + row_max + 1) // 2
        elif instr == "L":
          col_max = (col_min + col_max - 1) // 2
        elif instr == "R":
          col_min = (col_min + col_max + 1) // 2

      seat_ids.append(row_max * 8 + col_max)
    
    seat_ids_min = min(seat_ids)
    seat_ids_max = max(seat_ids)
    my_seat_id = None

    for i in range(seat_ids_min, seat_ids_max + 1):
      if i not in seat_ids:
        my_seat_id = i
        break
      
    return my_seat_id


def main():
  input_file = "day05-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()