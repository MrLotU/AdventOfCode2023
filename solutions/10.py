import re
from shapely.geometry import Point, Polygon

test_input = '''FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L'''

with open('inputs/10.txt', 'r') as f:
    _lines = f.read()

# _lines = test_input
lines = _lines.split('\n')

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == 'S':
            s_coord = (x, y)

adjacents = [
    ((-1, 0), ('F', 'L', '-')),
    ((1, 0), ('7', 'J', '-')),
    ((0, 1), ('L', 'J', '|')),
    ((0, -1), ('7', 'F', '|'))
]

print('---- DAY 10 PART 1 ----')

traversed_coords = [s_coord]

for coord, chars in adjacents:
    adj_coord = (s_coord[0] + coord[0], s_coord[1] + coord[1])
    if lines[adj_coord[1]][adj_coord[0]] in chars:
        traversed_coords.append(adj_coord)
        break

# print(traversed_coords)

relevant_map = {
    '-': [0, 1],
    '7': [0, 2],
    'J': [0, 3],
    'F': [1, 2],
    'L': [1, 3],
    '|': [2, 3],
    'S': []
}

while True:
    # print(traversed_coords)
    max_val = len(traversed_coords)
    
    x, y = traversed_coords[-1]
    # print(max_val, x, y, lines[y][x], s_coord, lines[s_coord[1]][s_coord[0]])
    
    if (x, y) == s_coord:
        break
    
    segment = lines[y][x]
    for i, (coord, chars) in enumerate(adjacents):
        if i not in relevant_map[segment]:
            continue
        adj_coord = (x + coord[0], y + coord[1])
        dest_char = lines[adj_coord[1]][adj_coord[0]]
        if adj_coord not in traversed_coords and dest_char in chars:
            # print(f'{lines[adj_coord[1]][adj_coord[0]]} connects to {segment}')
            traversed_coords.append(adj_coord)
            break
        elif dest_char == 'S':
            traversed_coords.append(adj_coord)

print(len(traversed_coords) // 2 - 1)

print('---- DAY 10 PART 2 ----')

found_points = []

coords = traversed_coords[:-1]
poly = Polygon(coords)

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if (x, y) not in traversed_coords:
            p = Point(x, y)
            if poly.contains(p):
                found_points.append((x, y))

print(found_points)
print(len(found_points))