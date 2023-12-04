import re

test_input = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

with open('inputs/4.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')

pattern = r'Card\s*(\d+):\s+((?:\s*\d+)+)\s+\|\s+((?:\s*\d+)+)'

print('---- DAY 4 PART 1 ----')

total = 0

for line in lines:
    _, wins, nums = re.match(pattern, line).groups()
    wins = [int(x) for x in re.findall('\d+', wins)]
    nums = [int(x) for x in re.findall('\d+', nums)]
    val = 0
    for num in nums:
        if num in wins:
            val = 1 if val == 0 else (val * 2)
    # print(line.split(': ')[0], val)
    total += val

print(total)

print('---- DAY 4 PART 2 ----')

total = 0
copies_of_cards = {}

for line in lines:
    card_id, wins, nums = re.match(pattern, line).groups()
    card_id = int(card_id)
    wins = [int(x) for x in re.findall('\d+', wins)]
    nums = [int(x) for x in re.findall('\d+', nums)]
    matches = sum([1 if n in wins else 0 for n in nums])

    copies_of_cards[card_id] = copies_of_cards.get(card_id, 0) + 1
    for i in range(card_id + 1, card_id + matches + 1):
        copies_of_cards[i] = copies_of_cards.get(i, 0) + (1 * copies_of_cards.get(card_id, 1))

print(sum(copies_of_cards.values()))
