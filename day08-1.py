#https://adventofcode.com/2020/day/8


def part1(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    instructions = []

    for line in lines:
      line_parts = line.split(" ")

      instruction = {}
      instruction["type"] = line_parts[0]
      instruction["visited"] = 0
      instruction["value"] = int(line_parts[1][1:])

      if line_parts[1][0] == "-":
        instruction["value"] *= -1
      
      instructions.append(instruction)

    accumulator = 0
    index = 0
    
    while instructions[index]["visited"] <= 0:
      instructions[index]["visited"] += 1
      
      if instructions[index]["type"] == "acc":
        accumulator += instructions[index]["value"]
        index += 1
      elif instructions[index]["type"] == "nop":
        index += 1
      elif instructions[index]["type"] == "jmp":
        index += instructions[index]["value"]

    return accumulator

    
def main():
  input_file = "day08-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()