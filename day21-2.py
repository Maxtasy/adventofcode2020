#https://adventofcode.com/2020/day/21
#ty, https://www.reddit.com/r/adventofcode/comments/khaiyk/2020_day_21_solutions/ggk9n51?utm_source=share&utm_medium=web2x&context=3

import fileinput as fi

with open("day21-input.txt", "r") as f:
  pos = {}
  for line in map(str.rstrip, f.readlines()):
      a, b = line.split(" (contains ")
      foods = set(a.split())
      algs = set(b[:-1].split(", "))

      for alg in algs:
          if alg not in pos:
              pos[alg] = foods.copy()
          else:
              pos[alg] &= foods


  taken = set()
  items = []
  while True:
      for alg, foods in pos.items():
          if len(foods - taken) == 1:
              o = min(foods-taken)
              items.append((alg,o))
              taken.add(o)
              break
      else:
          break

  print(",".join(x[1] for x in sorted(items)))