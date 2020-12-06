#https://adventofcode.com/2020/day/6


def part1(input_file):
  with open(input_file, "r") as f:
    groups = f.read().strip().split("\n\n")
    groups_array = []
    for group in groups:
      groups_array.append(group.split("\n"))
    
    yes_counts = []

    for group in groups_array:
      question_chars = []
      for person in group:
        for char in person:
          if char not in question_chars:
            question_chars.append(char)
      
      yes_counts.append(len(question_chars))
    
    return sum(yes_counts)
    


def main():
  input_file = "day06-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()