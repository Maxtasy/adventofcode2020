#https://adventofcode.com/2020/day/14
# ty, https://www.reddit.com/r/adventofcode/comments/kcr1ct/2020_day_14_solutions/gfs8m4f?utm_source=share&utm_medium=web2x&context=3


from collections import defaultdict


def allmasks(pos, mask):
  if not mask:
    yield 0
  else:
    if mask[-1] == '0':
      for m in allmasks(pos // 2, mask[:-1]):
        yield 2*m + pos % 2
    if mask[-1] == '1':
      for m in allmasks(pos // 2, mask[:-1]):
        yield 2*m + 1
    if mask[-1] == 'X':
      for m in allmasks(pos // 2, mask[:-1]):
        yield 2*m + 0
        yield 2*m + 1


def part2(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    mask = None
    addresses = defaultdict(int)
    for line in lines:
      op, arg = line.split(' = ')
      if op == 'mask':
        mask = arg
      else:
        pos = int(op[4:-1])
        # part 1:
        # mem[pos] = domask(int(arg), mask)
        for m in allmasks(pos, mask):
          addresses[m] = int(arg)
    
    return sum(addresses.values())

    
def main():
  input_file = "day14-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()