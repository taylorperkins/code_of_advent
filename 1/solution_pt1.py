

if __name__ == '__main__':
    start = 0

    with open('./input.txt') as f:
        for line in f.readlines():
            if line[0] == '-':
                start -= int(line[1:])
            else:
                start += int(line)

    print(start)
