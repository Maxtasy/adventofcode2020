#https://adventofcode.com/2020/day/7


def total_bags_inside_this_bag(bag_properties, color):
  if bag_properties[color]["empty"]:
    return 0
  else:
    count = 0
    for key in bag_properties[color]["inside_bags"].keys():
      count += bag_properties[color]["inside_bags"][key]
      count += bag_properties[color]["inside_bags"][key] * total_bags_inside_this_bag(bag_properties, key)

  return count


def part2(input_file):
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

      bag_properties[bag_color]["inside_bags"] = {}
      content_array = content_str.split(", ")

      for content_part in content_array:
        content_part_array = content_part.split(" ")
        count = int(content_part_array[0])
        inside_bag_color = content_part_array[1] + " " + content_part_array[2]

        bag_properties[bag_color]["inside_bags"][inside_bag_color] = count
    
    # print(bag_properties)
       
    return total_bags_inside_this_bag(bag_properties, "shiny gold")
    

def main():
  input_file = "day07-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()