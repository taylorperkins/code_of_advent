lowercase = list(map(chr, range(97, 123)))


class AlchemicalReduction(object):

    @classmethod
    def reduce_it(cls, data):
        index = 0
        while True:
            if not index:
                index += 1
                continue

            if index == len(data):
                break

            value = data[index]
            value_polarity = cls.polarity(value)

            previous_value = data[index - 1]
            prev_value_polarity = cls.polarity(previous_value)

            if cls.is_reactive(value, previous_value, value_polarity == prev_value_polarity):
                data = data[:index - 1] + data[index + 1:]
                index -= 1

            else:
                index += 1

        return data

    @staticmethod
    def polarity(value):
        if value in lowercase:
            return 1
        return 0

    @staticmethod
    def is_reactive(val1, val2, same_type):
        if not same_type and (val1.lower() == val2.lower()):
            return True
        return False


if __name__ == '__main__':
    with open('./input.txt') as f:
        line = f.read().splitlines()[0]

    counts = list()

    # this takes a while to run unfortunately. It may be better to get the unique lower letters in the line and iterate
    # over that first.. or to just exclude the letters from the process. Idk yet
    for lower_letter in lowercase:
        upper_letter = lower_letter.upper()

        reduced_line = [l for l in line if l not in [lower_letter, upper_letter]]

        new_line = AlchemicalReduction.reduce_it(reduced_line)

        counts.append(len(new_line))

    print(min(counts))
