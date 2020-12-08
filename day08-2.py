#https://adventofcode.com/2020/day/8


from copy import deepcopy


def part2(input_file):
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
    
    for i in range(len(instructions)):
      instructions_copy = deepcopy(instructions)

      if instructions_copy[i]["type"] == "acc":
        continue
      elif instructions_copy[i]["type"] == "jmp":
        instructions_copy[i]["type"] = "nop"
      elif instructions_copy[i]["type"] == "nop":
        instructions_copy[i]["type"] = "jmp"

      accumulator = 0
      index = 0
      
      while instructions_copy[index]["visited"] <= 0:
        instructions_copy[index]["visited"] += 1
        
        if instructions_copy[index]["type"] == "acc":
          accumulator += instructions_copy[index]["value"]
          index += 1
        elif instructions_copy[index]["type"] == "nop":
          index += 1
        elif instructions_copy[index]["type"] == "jmp":
          index += instructions_copy[index]["value"]
        
        if index >= len(instructions):
          return accumulator

    
def main():
  input_file = "day08-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()