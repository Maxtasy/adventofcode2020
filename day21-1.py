#https://adventofcode.com/2020/day/21
#ty, https://www.reddit.com/r/adventofcode/comments/khaiyk/2020_day_21_solutions/ggk9n51?utm_source=share&utm_medium=web2x&context=3


from collections import Counter
import itertools as it

all_foods = set()
times = Counter()

pos = {}

with open("day21-input.txt", "r") as f:
  for line in map(str.rstrip, f.readlines()):
      a, b = line.split(" (contains ")
      foods = set(a.split())
      algs = set(b[:-1].split(", "))

      all_foods |= foods
      times.update(foods)

      for alg in algs:
          if alg not in pos:
              pos[alg] = foods.copy()
          else:
              pos[alg] &= foods

  bad = set(it.chain.from_iterable(pos.values()))

  print(sum(times[food] for food in (all_foods - bad)))