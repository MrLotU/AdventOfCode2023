import re

test_input = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''

with open('inputs/1.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')

print('---- DAY 1 PART 1 ----')

total = 0

for line in lines:
    nums = re.findall(r'\d', line)
    if len(nums) == 0:
        continue
    a = nums[0]
    b = nums[-1]
    val = (ord(a) - 48) * 10 + (ord(b) - 48)
    # print(line, a, b, val)
    total += val

print(total)
    
print('---- DAY 1 PART 2 ----')

total = 0

NUM_MAP = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

pattern = '(?=(\d|{}))'.format('|'.join(NUM_MAP.keys()))

for line in lines:
    nums = re.findall(pattern, line)
    if len(nums) == 0:
        continue
    a = nums[0]
    a = (NUM_MAP[a] if a in NUM_MAP else (ord(a) - 48)) * 10
    b = nums[-1]
    b = NUM_MAP[b] if b in NUM_MAP else (ord(b) - 48)
    val = a + b
    # print(line, nums, a, b, val)
    total += val

print(total)