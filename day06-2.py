#https://adventofcode.com/2020/day/6


def part2(input_file):
  with open(input_file, "r") as f:
    groups = f.read().strip().split("\n\n")
    groups_array = []

    for group in groups:
      groups_array.append(group.split("\n"))
    
    yes_counts = []

    for group in groups_array:
      question_chars = {}
      yes_count = 0

      for person in group:
        for char in person:
          if not question_chars.get(char):
            question_chars[char] = 1
          else:
            question_chars[char] += 1
            
      for key in question_chars.keys():
        if question_chars[key] == len(group):
          yes_count += 1
      
      yes_counts.append(yes_count)
    
    return sum(yes_counts)
    


def main():
  input_file = "day06-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()