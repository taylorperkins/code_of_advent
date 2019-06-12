import re


def convert_value_to_numeric(value):
    if value == '.':
        return 0
    return 1


def convert_values_to_numeric(values):
    for value in values:
        yield convert_value_to_numeric(value)


def get_next_gen_from_map(pot_map, current_state):
    for i in range(len(current_state)):
        # can actually look back
        if tuple(current_state[i - 2:i + 3]) in pot_map:
            yield 1
        else:
            yield 0


if __name__ == '__main__':
    pot_map = dict()

    pattern = re.compile(r'(?P<pot_order>(#|.)+)\s=>\s(?P<pot_value>(#|.))')
    with open('./input.txt') as f:
        for line in f:
            m = re.match(pattern, line)

            pot_order = list(convert_values_to_numeric(m.group('pot_order')))
            pot_value = convert_value_to_numeric(m.group('pot_value'))

            pot_map[tuple(pot_order)] = pot_value

    initial_state = '...#..#.#..##......###...###..............'
    initial_numeric_state = list(convert_values_to_numeric(initial_state))
    print('{0:6d}: {1:4}'.format(0, str(initial_numeric_state)))

    for i in range(21):
        initial_numeric_state = list(get_next_gen_from_map(pot_map, initial_numeric_state))
        if 1 in initial_numeric_state[:3]:
            initial_numeric_state = [0] + initial_numeric_state

        if 1 in initial_numeric_state[-3:]:
            initial_numeric_state = initial_numeric_state + [0]

        print('{0:6d}: {1:4}'.format(i+1, str(initial_numeric_state)))

    counts = 0
    with open('./blah.txt') as f:
        for line in f:
            counts += line.count('#')

    print(counts)
