import re
from collections import defaultdict


if __name__ == '__main__':
    """This one took me a while to figure out.. then I had to step back (also sleep) and look at the bigger picture. 
    After doing that, it was a pretty easy one to solve (there are many ways to do the same thing!)

    Instead of counting cells, each cell acts as an id to a hash that keeps track of the patch_ids that are 
    layered on top of it.
    Once you have that.. you can pretty easily determine which patch's are going over multiple cells, 
    and which one never shared the cells it was touching. 
    """
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

    # This is the main logic
    for key, value in mapper.items():
        if len(value) > 1:
            overlapping_keys = overlapping_keys.union(value)
        else:
            island_keys = island_keys.union(value)

    # figures out the unique patch!
    print(island_keys.difference(overlapping_keys))

