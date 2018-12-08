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

    new_line = AlchemicalReduction.reduce_it(line)

    print(len(line), line)
    print(len(new_line), new_line)
