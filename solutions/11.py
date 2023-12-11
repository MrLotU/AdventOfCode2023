import itertools

test_input = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''

with open('inputs/11.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')

original_lines = lines[:]

inserts = []
for i in range(0, len(original_lines[0])):
    should_insert = True
    for line in original_lines:
        if line[i] == '#':
            should_insert = False
    if should_insert:
        inserts.append(i)
new_inserts = []

for i, line in enumerate(original_lines):
    for ins in inserts[::-1]:
        l = list(lines[i])
        l.insert(ins + 1, '.')
        lines[i] = ''.join(l)
    if '#' not in line:
        new_inserts.append(i)
        
for i in new_inserts[::-1]:
    lines.insert(i + 1, '.' * len(lines[0]))

print('---- DAY 11 PART 1 ----')

galaxies = []

def distance(a, b):
    xa, ya = a
    xb, yb = b
    
    return abs(xa - xb) + abs(ya - yb)

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '#':
            galaxies.append((x,y))

pairs = list(itertools.product(galaxies, galaxies))

distances = []
seen = set()
for a, b in pairs:
    if a == b or (a,b) in seen or (b,a) in seen:
        continue
    seen.add((a,b))
    distances.append(distance(a, b))

print(sum(distances))

print('---- DAY 11 PART 2 ----')

galaxies = []

for y, line in enumerate(original_lines):
    for x, char in enumerate(line):
        if char == '#':
            galaxies.append((x, y))

pairs = list(itertools.product(galaxies, galaxies))

GROWTH = 1_000_000

p2_distances = []

def part_two_distance(a, b):
    dist = distance(a,b)
    org = dist
    x_step = 1 if a[0] <= b[0] else -1
    y_step = 1 if a[1] <= b[1] else -1
    x_range = list(range(a[0], b[0], x_step))
    y_range = list(range(a[1], b[1], y_step))
    for ins in new_inserts:
        if ins in y_range:
            dist = dist - 1 + GROWTH

    for ins in inserts:
        if ins in x_range:
            dist = dist - 1 + GROWTH

    return dist

seen = set()
_seen = []
for a, b in pairs:
    if a == b or (a,b) in seen or (b,a) in seen:
        continue
    seen.add((a,b))
    _seen.append((a,b))
    p2_distances.append(part_two_distance(a, b))

print(sum(p2_distances))
