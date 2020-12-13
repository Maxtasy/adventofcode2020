#https://adventofcode.com/2020/day/13


# pip install sympy
from sympy.ntheory.modular import crt


def part2(input_file):
  with open(input_file, "r") as f:
    _, active_buses_str = f.read().strip().split("\n")

    modulos = []
    remainders = []

    busTimestamps = active_buses_str.split(",")
    for i in range(len(busTimestamps)):
        if busTimestamps[i].isnumeric():
            modulos.append(int(busTimestamps[i]))
            remainders.append((-i) % modulos[-1])

    return crt(modulos, remainders)
    
    
def main():
  input_file = "day13-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()