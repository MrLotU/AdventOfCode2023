import re

test_input = '''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#'''

with open('inputs/13.txt', 'r') as f:
    lines = f.read()

# lines = test_input
patterns = lines.split('\n\n')

print('---- DAY 13 PART 1 ----')

original_solutions = {}

def check_mirror(pattern, first_match):
    a, b = first_match
    assert abs(a - b) == 1, pattern[a] == pattern[b]
    right = len(pattern) - 1
    left = 0
    space_left = a - left
    space_right = right - b
    match = True
    for i in range(1, min(space_left, space_right) + 1):
        if pattern[a - i] != pattern[b + i]:
            match = False

    return match

def check_pattern(pattern):
    pattern_rows = pattern.split('\n')
    pattern_cols = [[row[x] for row in pattern_rows] for x in range(len(pattern_rows[0]))]
    
    answers = []
    
    for i, row in enumerate(pattern_rows):
        if i == 0:
            continue
        if row == pattern_rows[i-1] and check_mirror(pattern_rows, (i-1, i)):
            answers.append(100 * i)

    for i, col in enumerate(pattern_cols):
        if i == 0:
            continue
        if col == pattern_cols[i - 1] and check_mirror(pattern_cols, (i-1, i)):
            answers.append(i)

    if len(answers) == 1:
        return answers[0]
    elif len(answers) == 0:
        return None
    return answers

total = 0

for pattern in patterns:
    res = check_pattern(pattern)
    original_solutions[pattern] = res
    total += res

print(total)

print('---- DAY 13 PART 2 ----')

def replace_at_idx(s, idx, char):
    return s[:idx] + char + s[idx+1:]

total = 0

def do_part_two(pattern):
    for i, char in enumerate(pattern):
        if char in '.#':
            newchar = '.' if char == '#' else '#'
            newpattern = replace_at_idx(pattern, i, newchar)
            ress = check_pattern(newpattern)
            if ress is None:
                continue
            elif isinstance(ress, int):
                if original_solutions[pattern] != ress:
                    return ress
            else:
                for res in set(ress):
                    if original_solutions[pattern] != res:
                        return res


for pi, pattern in enumerate(patterns):
    total += do_part_two(pattern)

print(total)