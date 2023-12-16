import sys
sys.setrecursionlimit(10_000)

test_input = r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....'''

with open('inputs/16.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')

grid_height = len(lines)
grid_width = len(lines[0])

_grid = { (x, y): char for y, line in enumerate(lines) for x, char in enumerate(line) }

print('---- DAY 16 PART 1 ----')

DIRECTION = (1, 0)
START_COORD = (-1, 0)

def retrieve_energy(dir, start_loc):
    grid = { (x, y): char for y, line in enumerate(lines) for x, char in enumerate(line) }
    energized = { k: False for k in grid.keys() }
    do_not_loop = {}

    def follow_beam(direction, start):
        if (direction, start) in do_not_loop:
            return
        do_not_loop[(direction, start)] = True
        next_step = tuple(map(sum, zip(start, direction)))

        x, y = next_step
        dir_x, dir_y = direction
        if x >= grid_width or x <= -1 or y >= grid_height or y <= -1:
            return

        space = grid[next_step]
        
        energized[next_step] = True
        
        if space == '.' or (dir_x != 0 and space == '-') or (dir_y != 0 and space == '|'):
            return follow_beam(direction, next_step)
        elif space in ('\\', '/'):
            new_direction = (dir_y * -1, dir_x * -1) if space == '/' else (dir_y, dir_x)
            return follow_beam(new_direction, next_step)
        elif space in ('-', '|'):
            new_direction = (dir_y * -1, dir_x * -1)
            other_new_direction = (dir_y, dir_x)
            return (follow_beam(new_direction, next_step), follow_beam(other_new_direction, next_step))
        
    follow_beam(dir, start_loc)

    return sum(energized.values())

print(retrieve_energy(DIRECTION, START_COORD))

print('---- DAY 16 PART 2 ----')

inner_width = grid_width - 1
inner_height = grid_height - 1

every_edge = [(x, y) for x, y in _grid.keys() if x in (0,grid_width - 1) or y in (0, grid_height - 1)]
corners = [(0, 0), (0, inner_height), (inner_width, 0), (inner_width, inner_height)]

result = 0

for first_point in every_edge:
    x, y = first_point
    
    if first_point in corners:
        combis = [(x, y - 1 if y == 0 else y + 1 if y == inner_height else y), (x - 1 if x == 0 else x + 1 if x == inner_width else x, y)]
        for x, y in combis:
            x_mult = 1 if x == -1 else -1
            y_mult = 1 if y == -1 else -1

            start_direction = (x_mult if x in (-1, grid_width) else 0, y_mult if y in (-1, grid_height) else 0)
            
            result = max(result, retrieve_energy(start_direction, (x, y)))
        
    x = x - 1 if x == 0 else x + 1 if x == inner_width else x
    y = y - 1 if y == 0 else y + 1 if y == inner_height else y

    x_mult = 1 if x == -1 else -1
    y_mult = 1 if y == -1 else -1

    start_direction = (x_mult if x in (-1, grid_width) else 0, y_mult if y in (-1, grid_height) else 0)
    
    result = max(result, retrieve_energy(start_direction, (x, y)))

print(result)