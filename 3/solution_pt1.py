import re
from collections import defaultdict


if __name__ == '__main__':
    """This one was a pretty straightforward problem I thought, but couldn't be calculated
    until all of the patches had been iterated over.
    
    Iterate over each patch plan, and "draw" out the patch.
    Keep track of the cell you are on, and count how many patches go over it.
    
    Finally, go over the results and figure out the cells that had multiple patches.
    """

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

    # If the cell had multiple patches, add to the sq_inch
    sq_inch = 0
    for i_val in mapper.values():
        for j_val in i_val.values():
            if j_val > 1:
                sq_inch += 1

    print(sq_inch)
