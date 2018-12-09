

if __name__ == '__main__':
    """Pretty straightforward approach to solving this one.
    If the line starts with a '-', subtract it from total, else add it.
    """
    start = 0

    with open('./input.txt') as f:
        for line in f.readlines():
            if line[0] == '-':
                start -= int(line[1:])
            else:
                start += int(line)

    print(start)
