import re
from collections import defaultdict


if __name__ == '__main__':

    mapper = dict()

    with open('./input.txt', 'r') as f:
        for line in f.readlines():
            m = re.search(r'@ (?P<start_col>\d+),(?P<start_row>\d+): (?P<width>\d+)x(?P<height>\d+)', line)

            overlaps_patch = False

            for i in range(int(m.group('start_row')), int(m.group('start_row')) + int(m.group('height'))):
                if i not in mapper:
                    mapper[i] = defaultdict(int)

                for j in range(int(m.group('start_col')), int(m.group('start_col')) + int(m.group('width'))):
                    mapper[i][j] += 1

    sq_inch = 0
    for i_val in mapper.values():
        for j_val in i_val.values():
            if j_val > 1:
                sq_inch += 1

    print(sq_inch)
