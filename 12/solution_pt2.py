import re

from collections import defaultdict


def convert_value_to_numeric(value):
    if value == '.':
        return 0
    return 1


def convert_values_to_numeric(values):
    for value in values:
        yield convert_value_to_numeric(value)


def add_vals_to_map(pot_list, pot_counter, ind):
    for i in range(ind, len(pot_list) + ind):
        pot_counter[i] += pot_list[i + abs(ind)]


def get_next_gen_from_map(rules, current_state):
    for i in range(len(current_state)):
        # can actually look back
        if tuple(current_state[i - 2:i + 3]) in rules:
            yield 1
        else:
            yield 0


if __name__ == '__main__':
    rules = dict()

    pattern = re.compile(r'(?P<pot_order>(#|.)+)\s=>\s(?P<pot_value>(#|.))')
    with open('./input.txt') as f:
        for line in f:
            m = re.match(pattern, line)

            pot_order = list(convert_values_to_numeric(m.group('pot_order')))
            pot_value = convert_value_to_numeric(m.group('pot_value'))

            rules[tuple(pot_order)] = pot_value

    pot_start = '##.######...#.##.#...#...##.####..###.#.##.#.##...##..#...##.#..##....##...........#.#.#..###.#'

    ind = 0

    pot_counter = defaultdict(int)
    pot_values_to_numeric = list(convert_values_to_numeric(pot_start))

    if 1 in pot_values_to_numeric[:2]:
        pot_values_to_numeric = [0, 0] + pot_values_to_numeric
        ind -= 2

    if 1 in pot_values_to_numeric[-2:]:
        pot_values_to_numeric = pot_values_to_numeric + [0, 0]

    add_vals_to_map(pot_values_to_numeric, pot_counter, ind)
    print('{0:6d}: {1:4}'.format(0, str(pot_values_to_numeric)))

    for i in range(20):
        pot_values_to_numeric = list(get_next_gen_from_map(rules, pot_values_to_numeric))

        if 1 in pot_values_to_numeric[:3]:
            pot_values_to_numeric = [0] + pot_values_to_numeric
            ind -= 1

        if 1 in pot_values_to_numeric[-3:]:
            pot_values_to_numeric = pot_values_to_numeric + [0]

        add_vals_to_map(pot_values_to_numeric, pot_counter, ind)
        print('{0:6d}: {1:4}'.format(i + 1, str(pot_values_to_numeric)))

    total = 0
    for i in range(min(pot_counter), max(pot_counter)):
        if pot_values_to_numeric[i + abs(ind)]:
            total += i

    print(total)
