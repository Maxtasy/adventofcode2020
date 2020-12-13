#https://adventofcode.com/2020/day/13


def part1(input_file):
  with open(input_file, "r") as f:
    arrival_timestamp, active_buses_str = f.read().strip().split("\n")

    active_buses = active_buses_str.split(",")
    
    minimum_waiting_time = 10000000
    bus_id = None

    for bus in active_buses:
      if bus == "x":
        continue

      timestamp = 0

      while timestamp < int(arrival_timestamp):
        timestamp += int(bus)
      
      waiting_time = timestamp - int(arrival_timestamp)

      if waiting_time < minimum_waiting_time:
        minimum_waiting_time = waiting_time
        bus_id = int(bus)
    
    return bus_id * minimum_waiting_time

    
def main():
  input_file = "day13-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()