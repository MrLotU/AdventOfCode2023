import re
from itertools import islice

test_input = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''

with open('inputs/14.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')

cols = [[row[x] for row in lines] for x in range(len(lines[0]))]

print('---- DAY 14 PART 1 ----')

def calc_load(cols):
    total_height = len(cols[0])
    total_load = 0

    for col in cols:
        col_load = 0
        block_idx = -1
        for idx, object in enumerate(col):
            if object == '#':
                block_idx = idx
            elif object == 'O':
                block_idx += 1
                col_load += total_height - block_idx
            
        total_load += col_load
    return total_load

print(calc_load(cols))

print('---- DAY 14 PART 2 ----')

SPIN = ['N', 'W', 'S', 'E']
SPINS = 1_000_000_000

def move_in_direction(grid, direction):
    cols = [[row[x] for row in grid] for x in range(len(grid[0]))]
    
    working_lines = cols if direction in ['N', 'S'] else grid
    step = 1 if direction in ['N', 'W'] else -1
    rev_step = step * -1
    indices = list(range(0, len(working_lines[0])))

    for line_idx, line in enumerate(working_lines):
        copy = line[:]
        first_empty = indices[::step][0] + rev_step
        for idx in indices[::step]:
            if line[idx] == '#':
                first_empty = idx
            elif line[idx] == 'O':
                first_empty += step
                copy[idx] = '.'
                copy[first_empty] = 'O'
        working_lines[line_idx] = copy


    if direction in ['N', 'S']:
        working_lines = [ [col[x] for col in working_lines] for x in range(len(working_lines[0]))]
        
    return working_lines


mutable_lines = list(map(list, lines))

seen = {}

for i in range(SPINS):
    print(f'Cycle {i:_}')
    
    t = tuple([tuple(x)for x in mutable_lines])
    if t in seen:
        prev_i = seen[t]
        length = i - prev_i
        target = prev_i + ((SPINS - prev_i) % length)
        
        mutable_lines = next(islice(seen.keys(), target, target + 1))
        break
    
    seen[t] = i
    
    for dir in SPIN:
        mutable_lines = move_in_direction(mutable_lines, dir)

print(sum(row_load * row.count("O")for row_load, row in zip(range(len(mutable_lines), 0, -1), mutable_lines)))
