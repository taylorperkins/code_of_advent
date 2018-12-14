from collections import defaultdict


POWER_MAP = dict()
SIZE_POWER_MAP = defaultdict(dict)


def calculate_cell_power_level(x, y, serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level = str(power_level * rack_id)

    if len(power_level) > 2:
        return int(power_level[-3]) - 5
    return -5


def calculate_grid_power_level(x, y, serial_number, size):
    grid_sum = 0

    if size > 1:
        grid_sum += SIZE_POWER_MAP[size - 1][(x, y)]

        final_column = x + size - 1
        final_row = y + size - 1

        for i in range(size):
            grid_sum += POWER_MAP[(final_column, y + i)]

        for i in range(size - 1):
            grid_sum += POWER_MAP[(x + i, final_row)]

    else:
        cell_power = calculate_cell_power_level(x, y, serial_number)
        POWER_MAP[(x, y)] = cell_power
        grid_sum += cell_power

    return grid_sum


if __name__ == '__main__':
    """Overall, this takes a little while to run. But as the size increases, the speed gets exponentially faster"""
    serial_number = 1788

    # this is the nxn size of the matrix
    # each size uses the sum from the previous size at the same point + right and bottom edge values
    # for the final power. It doesn't re-calculate the powers
    for size in range(1, 301):
        for x in range(1, 301 - size + 1):
            for y in range(1, 301 - size + 1):
                SIZE_POWER_MAP[size][(x, y)] = calculate_grid_power_level(x, y, serial_number, size)

        if size % 10 == 0:
            print(size)

    final_coords, final_size, highest_power = None, None, 0
    for size, vals in SIZE_POWER_MAP.items():
        for coords, power in vals.items():
            if final_coords == None:
                final_coords = coords
                final_size = size
                highest_power = power
            else:
                if power > highest_power:
                    final_coords = coords
                    final_size = size
                    highest_power = power

    print(f'Size: {final_size}\t Coords: {final_coords}\tPower: {highest_power}')
