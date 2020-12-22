#https://adventofcode.com/2020/day/19
#ty, https://www.reddit.com/r/adventofcode/comments/kg1mro/2020_day_19_solutions/ggc1jb5?utm_source=share&utm_medium=web2x&context=3


import re


def getre(rulenum, rules):
    if rulenum == '8':
        return getre('42', rules) + '+'
    elif rulenum == '11':
        a = getre('42', rules)
        b = getre('31', rules)
        return '(?:' + '|'.join(f'{a}{{{n}}}{b}{{{n}}}' for n in range(1, 100)) + ')'

    rule = rules[rulenum]
    if re.fullmatch(r'"."', rule):
        return rule[1]
    else:
        parts = rule.split(' | ')
        res = []
        for part in parts:
            nums = part.split(' ')
            res.append(''.join(getre(num, rules) for num in nums))
        return '(?:' + '|'.join(res) + ')'


def part2(input_file):
  with open(input_file, "r") as f:
    rules, strings = [l.rstrip('\n') for l in f.read().split('\n\n')]

    rules = dict([rule.split(': ', 1) for rule in rules.split('\n')])

    z = getre('0', rules)
    count = 0
    for string in strings.split('\n'):
        count += bool(re.fullmatch(z, string))

    return count


def main():
  input_file = "day19-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()