import re
import functools

test_input = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''

with open('inputs/15.txt', 'r') as f:
    lines = f.read()

# lines = test_input
sequences = lines.split(',')

print('---- DAY 15 PART 1 ----')

total = 0

def do_hash(seq):
    return functools.reduce(lambda x, y: ((x + ord(y)) * 17) % 256, seq, 0)

for seq in sequences:
    total += do_hash(seq)

print(total)

print('---- DAY 15 PART 2 ----')

boxes = { x: [] for x in range(256) }

for seq in sequences:
    label = seq[:-2] if '=' in seq else seq[:-1]
    op = '=' if '=' in seq else '-'
    val = seq[-1]
    
    box = do_hash(label)
    if op == '-':
        for i, x in list(enumerate(boxes[box]))[::-1]:
            if x[0] == label:
                boxes[box].pop(i)
    elif op == '=':
        val = int(val)
        inserted = False
        for i, x in enumerate(boxes[box]):
            if x[0] == label:
                boxes[box][i] = (label, val)
                inserted = True
        if not inserted:
            boxes[box].append((label, val))

total = 0

for k, v in boxes.items():
    for i, (l, fl) in enumerate(v):
        total += (k + 1) * (i + 1) * fl

print(total)