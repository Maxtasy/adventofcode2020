#https://adventofcode.com/2020/day/18
#ty, https://www.reddit.com/r/adventofcode/comments/kfeldk/2020_day_18_solutions/gg8162d?utm_source=share&utm_medium=web2x&context=3


class T:
  def __init__(self, v):
    self.v = v
  def __add__(self, other):
    return T(self.v + other.v)
  def __sub__(self, other):
    return T(self.v * other.v)
  def __mul__(self, other):
    return T(self.v + other.v)


def part1(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    total = 0
    for line in lines:
      for d in range(10):
        line = line.replace(f"{d}", f"T({d})")
      line = line.replace("*", "-")

      total += eval(line, {"T": T}).v
    
    return total


def main():
  input_file = "day18-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()