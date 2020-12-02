#https://adventofcode.com/2020/day/2


def is_valid_pw(pw, letter, pos1, pos2):
  pos1 = int(pos1) - 1
  pos2 = int(pos2) - 1
  
  if (pw[pos1] == letter and not pw[pos2] == letter) or (pw[pos2] == letter and not pw[pos1] == letter):
    return True
  else:
    return False


def part2(input_file):
  with open(input_file, "r") as f:
    input_str = f.read().strip().split("\n")
    valid_password_count = 0
    for line in input_str:
      line = line.split(" ")
      pw = line[2]
      letter = line[1][0]
      pos1, pos2 = line[0].split("-")
      if is_valid_pw(pw, letter, pos1, pos2):
        valid_password_count += 1
    
    return valid_password_count


def main():
  input_file = "day02-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()