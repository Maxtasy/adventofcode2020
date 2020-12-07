#https://adventofcode.com/2020/day/7


def bag_contains_golden_bag(bag_properties, color):
  if bag_properties[color]["empty"]:
    return False
  elif bag_properties[color]["contains_gold"]:
    return True
  else:
    for key in bag_properties[color]["inside_bags"].keys():
      if bag_contains_golden_bag(bag_properties, key):
        bag_properties[color]["contains_gold"] = True
        return True


def part1(input_file):
  with open(input_file, "r") as f:
    rules = f.read().strip().split("\n")
    bag_properties = {}

    for rule in rules:
      bag_color, content_str = rule.split(" bags contain ")
      bag_properties[bag_color] = {}

      if content_str == "no other bags.":
        bag_properties[bag_color]["empty"] = True
        continue
      else:
        bag_properties[bag_color]["empty"] = False

      bag_properties[bag_color]["contains_gold"] = False
      bag_properties[bag_color]["inside_bags"] = {}
      content_array = content_str.split(", ")

      for content_part in content_array:
        content_part_array = content_part.split(" ")
        count = int(content_part_array[0])
        inside_bag_color = content_part_array[1] + " " + content_part_array[2]

        if (inside_bag_color == "shiny gold"):
          bag_properties[bag_color]["contains_gold"] = True

        bag_properties[bag_color]["inside_bags"][inside_bag_color] = count
    
    count = 0

    for color in bag_properties.keys():
      if bag_contains_golden_bag(bag_properties, color):
        count += 1
    
    return count
    


def main():
  input_file = "day07-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()