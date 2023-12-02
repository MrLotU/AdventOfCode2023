import re

test_input = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

with open('inputs/2.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')

print('---- DAY 2 PART 1 ----')

limitts = {
    'blue': 14,
    'red': 12,
    'green': 13
}

total = 0

for line in lines:
    maxes = {
        'blue': 0,
        'red': 0,
        'green': 0
    }
    for val, color in re.findall(r'(\d+) (blue|green|red)', line):
        maxes[color] = max(maxes[color], int(val))
    valid = True
    for k, v in maxes.items():
        if v > limitts[k]:
            valid = False
    if valid:
        total += int(re.findall(r'\d+', line)[0])
    
print(total)
    

print('---- DAY 2 PART 2 ----')

total = 0

for line in lines:
    maxes = {
        'blue': 0,
        'red': 0,
        'green': 0
    }
    for val, color in re.findall(r'(\d+) (blue|green|red)', line):
        maxes[color] = max(maxes[color], int(val))
    
    total += (maxes['blue'] * maxes['green'] * maxes['red'])
    
print(total)