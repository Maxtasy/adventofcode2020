#https://adventofcode.com/2020/day/16


def part1(input_file):
  with open(input_file, "r") as f:
    input_parts = f.read().strip().split("\n\n")

    rules = {}

    for line in input_parts[0].split("\n"):
      name, rest = line.split(": ")
      rest_parts = rest.split(" ")
      range1_min, range1_max = list(map(int, rest_parts[0].split("-")))
      range2_min, range2_max = list(map(int, rest_parts[2].split("-")))
      rules[name] = (range1_min, range1_max, range2_min, range2_max)
    
    my_ticket = list(map(int, (input_parts[1].split("\n")[1].split(","))))

    ticket_lines = input_parts[2].split(":\n")[1].split("\n")
    tickets = []
    for ticket_line in ticket_lines:
      ticket = list(map(int, ticket_line.split(",")))
      tickets.append(ticket)

    error_rate = 0

    for ticket in tickets:
      for num in ticket:
        valid = False
        for key in rules.keys():
          if ((num >= rules[key][0] and num <= rules[key][1]) or 
              (num >= rules[key][2] and num <= rules[key][3])):
            valid = True
            break
        if not valid:
          error_rate += num
          break
    
    return error_rate


def main():
  input_file = "day16-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()