#https://adventofcode.com/2020/day/16


def part2(input_file):
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

    valid_tickets = []

    for ticket in tickets:
      valid_ticket = True
      for num in ticket:
        num_valid = False
        for key in rules.keys():
          if ((num >= rules[key][0] and num <= rules[key][1]) or 
              (num >= rules[key][2] and num <= rules[key][3])):
            num_valid = True
            break
        if not num_valid:
          valid_ticket = False
          break
      
      if valid_ticket:
        valid_tickets.append(ticket[:])

    fields = []

    for i in range(len(my_ticket)):
      field = []
      for ticket in valid_tickets:
        field.append(ticket[i])
      fields.append(field)
    
    field_names = {}
    
    while len(rules) > 0:
      for i in range(len(fields)):
        impossible_names = []
        for num in fields[i]:
          for name in list(rules.keys()):
            if not ((num >= rules[name][0] and num <= rules[name][1]) or (num >= rules[name][2] and num <= rules[name][3])):
              if name not in impossible_names:
                impossible_names.append(name)
        possible = []
        for key in list(rules.keys()):
          if key not in impossible_names:
            possible.append(key)
      
        if len(possible) == 1:
          field_names[i] = possible[0]
          del rules[possible[0]]
    
    ids_with_departure = []
    for key in field_names.keys():
      if "departure" in field_names[key]:
        ids_with_departure.append(key)
    
    product = 1
    for id in ids_with_departure:
      product *= my_ticket[id]
    
    return product


def main():
  input_file = "day16-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()