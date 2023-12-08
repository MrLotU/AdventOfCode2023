import re
import math

test_input = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''

with open('inputs/8.txt', 'r') as f:
    lines = f.read()

instructions = lines.split('\n')[0]
nodes = {x[0]: (x[1], x[2]) for x in re.findall(r'(\w{3}) = \((\w{3}), (\w{3})\)', lines)}

print('---- DAY 8 PART 1 ----')

loc = 'AAA'
steps = 0

while loc != 'ZZZ':
    ins = instructions[steps % len(instructions)]
    loc = nodes[loc][0 if ins == 'L' else 1]
    
    steps += 1

print(steps)

print('---- DAY 8 PART 2 ----')

relevant_nodes = [n for n in nodes.keys() if n[-1] == 'A']

def _next(node, step):
    ins = instructions[step % len(instructions)]
    return nodes[node][0 if ins == 'L' else 1]

def complete_one_loop(node):
    loc = node
    step = 0
    while loc != node or step == 0:
        loc = _next(loc, step)
        step += 1
        if loc[-1] == 'Z':
            return step

first_z_vals = list(map(complete_one_loop, relevant_nodes))

print(math.lcm(*first_z_vals))
