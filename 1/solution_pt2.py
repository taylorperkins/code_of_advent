from collections import Counter


if __name__ == '__main__':
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
