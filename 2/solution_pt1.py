from collections import Counter


if __name__ == '__main__':
    twos = 0
    threes = 0

    with open('./input.txt', 'r') as f:
        for line in f.readlines():
            line_counter = Counter()

            for letter in line:
                line_counter[letter] += 1

            has_two = False
            has_three = False

            for value in line_counter.values():
                if value == 2:
                    has_two = True

                elif value == 3:
                    has_three = True

            if has_two:
                twos += 1

            if has_three:
                threes += 1

    print(twos * threes)
