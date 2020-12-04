#https://adventofcode.com/2020/day/4


def transform_entry(l):
  l = l.replace("\n", " ").split(" ")
  entry = {}
  for item in l:
    key, value = item.split(":")
    entry[key] = value
  return entry


def is_valid(entry):
  required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
  for field in required_fields:
    if field not in entry.keys():
      return False
  return True


def part1(input_file):
  with open(input_file, "r") as f:
    entries = f.read().strip().split("\n\n")
    entries = list(map(transform_entry, entries))

    valid_passports = 0

    for entry in entries:
      if is_valid(entry):
        valid_passports += 1
  
  return valid_passports


def main():
  input_file = "day04-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()