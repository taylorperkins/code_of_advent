from collections import Counter


if __name__ == '__main__':
    """Here, we are basically categorizing lines in a file: if they contain a letter two or three times.
    
    The final result is the number of lines that contain 2 of the same letters multiplied by the 
    umber of lines that contain 3 of the same letter.
    """

    twos = 0
    threes = 0

    with open('./input.txt', 'r') as f:
        for line in f.readlines():
            line_counter = Counter()

            has_two = False
            has_three = False
            for letter in line:
                line_counter[letter] += 1

                if line_counter[letter] == 2:
                    has_two = True

                elif line_counter[letter] == 3:
                    has_three = True

            if has_two:
                twos += 1

            if has_three:
                threes += 1

    print(twos * threes)
