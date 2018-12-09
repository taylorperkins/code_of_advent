from collections import Counter


if __name__ == '__main__':
    """Most of the code used from the first solution.
    If the line starts with a '-', subtract it from total, else add it.
    
    Catch here, is that we want to keep track of the number of times start is at a value.
    Once it hits a number twice, break out of the loop.
    Also tricky because you need to loop over the contents of the file a couple times!
    """
    counter = Counter({0: 1})

    start = 0
    found = False
    while not found:
        with open('./input.txt') as f:
            for line in f.readlines():
                if line[0] == '-':
                    start -= int(line[1:])

                else:
                    start += int(line)

                counter[start] += 1

                if counter[start] == 2:
                    found = True
                    break

    print(start)
