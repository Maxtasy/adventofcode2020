#https://adventofcode.com/2020/day/22


from collections import deque


def part1(input_file):
  with open(input_file, "r") as f:
    players_arr = f.read().strip().split("\n\n")

    card_stacks = []

    for i in range(len(players_arr)):
      cards = deque(list(map(int, players_arr[i].split("\n")[1:])))
      card_stacks.append(cards)
    
    while len(card_stacks[0]) != 0 and len(card_stacks[1]) != 0:
      player_card = card_stacks[0].popleft()
      crab_card = card_stacks[1].popleft()
      if player_card > crab_card:
        card_stacks[0].append(player_card)
        card_stacks[0].append(crab_card)
      else:
        card_stacks[1].append(crab_card)
        card_stacks[1].append(player_card)
    
    answer = 0
    multiplicator = 1
    for i in range(len(card_stacks[0])-1, -1, -1):
      answer += multiplicator * card_stacks[0][i]
      multiplicator += 1

    return answer


def main():
  input_file = "day22-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()