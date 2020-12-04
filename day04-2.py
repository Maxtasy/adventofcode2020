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
  valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

  for field in required_fields:
    if field not in entry.keys():
      return False

  if len(entry["byr"]) != 4 or int(entry["byr"]) < 1920 or int(entry["byr"]) > 2002:
    return False

  if len(entry["iyr"]) != 4 or int(entry["iyr"]) < 2010 or int(entry["iyr"]) > 2020:
    return False

  if len(entry["eyr"]) != 4 or int(entry["eyr"]) < 2020 or int(entry["eyr"]) > 2030:
    return False

  if entry["hgt"][-2:] == "cm":
    height = int(entry["hgt"][:-2])
    if height < 150 or height > 193:
      return False
  elif entry["hgt"][-2:] == "in":
    height = int(entry["hgt"][:-2])
    if height < 59 or height > 76:
      return False
  else:
    return False

  if entry["hcl"][0] != "#" or len(entry["hcl"]) != 7:
    return False
  else:
    for char in entry["hcl"][1:]:
      if char not in "0123456789abcdef":
        return False

  if entry["ecl"] not in valid_eye_colors:
    return False
  
  if len(entry["pid"]) != 9:
    return False
  else:
    for char in entry["pid"]:
      if char not in "0123456789":
        return False
    
  return True


def part2(input_file):
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
  print(part2(input_file))


if __name__ == "__main__":
  main()