#https://adventofcode.com/2020/day/2


def is_valid_pw(pw, letter, min_count, max_count):
  min_count = int(min_count)
  max_count = int(max_count)
  letter_count = 0
  for char in pw:
    if char == letter:
      letter_count += 1
  
  if letter_count >= min_count and letter_count <= max_count:
    return True
  else:
    return False


def part1(input_file):
  with open(input_file, "r") as f:
    input_str = f.read().strip().split("\n")
    valid_password_count = 0
    for line in input_str:
      line = line.split(" ")
      pw = line[2]
      letter = line[1][0]
      min_count, max_count = line[0].split("-")
      if is_valid_pw(pw, letter, min_count, max_count):
        valid_password_count += 1
    
    return valid_password_count


def main():
  input_file = "day02-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()