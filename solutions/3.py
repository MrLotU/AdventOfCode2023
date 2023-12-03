import re

test_input = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

with open('inputs/3.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')

print('---- DAY 3 PART 1 ----')

adjacents = [
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1)
]

current_number_builder = ''
should_add_num = False
total = 0

for line_idx, line in enumerate(lines):
    for char_idx, char in enumerate(line):
        if char in '0123456789':
            current_number_builder += char
            for a,b in adjacents:
                try:
                    if lines[abs(line_idx + b)][abs(char_idx + a)] not in '.0123456789':
                        should_add_num = True
                except:
                    pass
        else:
            if should_add_num and current_number_builder != '':
                # print(f'Adding {int(current_number_builder)}')
                total += int(current_number_builder)
            should_add_num = False
            current_number_builder = ''

print(total)

print('---- DAY 3 PART 2 ----')

current_number_builder = ''
adjacent_gears = set()
gears = {}
total = 0

for line_idx, line in enumerate(lines):
    for char_idx, char in enumerate(line):
        if char in '0123456789':
            current_number_builder += char
            for a,b in adjacents:
                try:
                    if lines[abs(line_idx + b)][abs(char_idx + a)] == '*':
                        adjacent_gears.add((abs(line_idx + b), abs(char_idx + a)))
                except:
                    pass
        else:
            if adjacent_gears != []:
                for coord in adjacent_gears:
                    gears[coord] = gears.get(coord, []) + [int(current_number_builder)]
            adjacent_gears = set()
            current_number_builder = ''

for v in gears.values():
    if len(v) == 2:
        total += (v[0] * v[1])

print(total)