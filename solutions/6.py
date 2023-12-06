import re
import functools

test_input = '''Time:      7  15   30
Distance:  9  40  200'''

with open('inputs/6.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')

races = zip([int(x) for x in re.findall(r'\d+',  lines[0])], [int(x) for x in re.findall(r'\d+', lines[1])])

print('---- DAY 6 PART 1 ----')

wins = []

for race_time, record in races:
    possible = 0
    for i in range(0, race_time + 1):
        if i * (race_time - i) > record:
            # print(f'Win possible holding button for {i} seconds. Distance will be {i * (race_time - i)}')
            possible += 1

    wins.append(possible)
    print(race_time, record, possible * 2, wins)

print(wins)

print(functools.reduce(lambda x, y: x * y, wins, 1))

print('---- DAY 6 PART 2 ----')

race_time = int(lines[0].split(':')[1].replace(' ', ''))
record = int(lines[1].split(':')[1].replace(' ', ''))

print(race_time, record)
impossibles = 0
for i in range(0, race_time + 1):
    if i * (race_time - i) <= record:
        impossibles += 1
    else:
        break

print(race_time + 1 - impossibles * 2)