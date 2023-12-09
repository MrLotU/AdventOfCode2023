import re

test_input = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''

with open('inputs/9.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')

print('---- DAY 9 PART 1 ----')

total = 0

for i, line in enumerate(lines):
    nums = list(map(int, re.findall(r'-?\d+', line)))
    maps = [nums]
    while set(maps[-1]) != set([0]):
        n = maps[-1]
        maps.append([ n[i+1] - x for i, x in enumerate(n[:-1]) ])
    
    for i in range(len(maps) - 2, -1, -1):
        maps[i].append(maps[i][-1] + maps[i + 1][-1])
    
    total += maps[0][-1]

print(total)

print('---- DAY 9 PART 2 ----')

total = 0

for i, line in enumerate(lines):
    nums = list(map(int, re.findall(r'-?\d+', line)))
    maps = [nums]
    while set(maps[-1]) != set([0]):
        n = maps[-1]
        maps.append([ n[i+1] - x for i, x in enumerate(n[:-1]) ])
    
    for i in range(len(maps) - 2, -1, -1):
        maps[i] = [maps[i][0] - maps[i + 1][0]] + maps[i]
    
    total += maps[0][0]

print(total)
