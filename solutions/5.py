import re

test_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

with open("inputs/5.txt", "r") as f:
    lines = f.read()

# lines = test_input
lines = lines.split("\n\n")

print("---- DAY 5 PART 1 ----")

seeds = [int(x) for x in re.findall(r"\d+", lines[0])]
print(seeds)

maps = {}
order = [
    "seed",
    "soil",
    "fertilizer",
    "water",
    "light",
    "temperature",
    "humidity",
    "location",
]
for line in lines[1:]:
    id = line.split(" ")[0]
    nums = re.findall(r"^(\d+) (\d+) (\d+)$", line, re.M)

    maps[id] = [[int(y) for y in x] for x in nums]

print(maps)

locs = []

for seed in seeds:
    val = seed
    # print(f"Starting seed {seed}")
    for i, o in enumerate(order[:-1]):
        dest = order[i + 1]
        key = f"{o}-to-{dest}"
        sections = maps[key]
        for dest_start, source_start, size in sections:
            if val >= source_start and val < source_start + size:
                offset = val - source_start
                val = dest_start + offset
                # print(f'Match for {seed} step {key}')
                break
        # print(f"\tSeed {seed} after step {key} is {val}")
    # print(f"Location for {seed} is {val}")
    locs.append(val)

print(min(locs))

print("---- DAY 5 PART 2 ----")

seed_ranges = [(int(x) for x in y) for y in re.findall(r"(\d+) (\d+)", lines[0])]

for m in maps.values():
    
    new_seeds = []
    for start, size in seed_ranges:
        while size != 0:
            matched = False
            closest = size
            
            for dest, source, map_size in m:
                if source <= start < source + map_size:
                    offset = start - source
                    remaining = min(map_size - offset, size)
                    new_seeds.append((dest+offset, remaining))
                    start += remaining
                    size -= remaining
                    matched = True
                    break
                else:
                    if start < source:
                        closest = min(source - start, closest)
            
            if not matched:
                keep_len = min(closest, size)
                new_seeds.append((start, keep_len))
                start += keep_len
                size -= keep_len
            
    seed_ranges = new_seeds

print(min(x[0] for x in seed_ranges))