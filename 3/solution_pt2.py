import re
from collections import defaultdict


if __name__ == '__main__':

    mapper = defaultdict(set)

    with open('./input.txt', 'r') as f:
        for line in f.readlines():
            m = re.search(r'#(?P<id>\d+) @ (?P<start_col>\d+),(?P<start_row>\d+): (?P<width>\d+)x(?P<height>\d+)', line)

            overlaps_patch = False

            for i in range(int(m.group('start_row')), int(m.group('start_row')) + int(m.group('height'))):
                for j in range(int(m.group('start_col')), int(m.group('start_col')) + int(m.group('width'))):
                    mapper[(i, j)].add(m.group('id'))

    island_keys = set()
    overlapping_keys = set()

    for key, value in mapper.items():
        if len(value) > 1:
            overlapping_keys = overlapping_keys.union(value)
        else:
            island_keys = island_keys.union(value)

    print(island_keys.difference(overlapping_keys))

