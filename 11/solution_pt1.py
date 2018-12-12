POWER_MAP = dict()


def calculate_cell_power_level(x, y, serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level = str(power_level * rack_id)

    if len(power_level) > 2:
        return int(power_level[-3]) - 5
    return -5


def calculate_grid_power_level(x, y, serial_number):
    grid_sum = 0

    for i in range(3):
        cell_x = x + i
        for j in range(3):
            cell_y = y + j

            if (cell_x, cell_y) in POWER_MAP:
                grid_sum += POWER_MAP[(cell_x, cell_y)]

            else:
                cell_power = calculate_cell_power_level(cell_x, cell_y, serial_number)
                POWER_MAP[(cell_x, cell_y)] = cell_power
                grid_sum += cell_power

    return grid_sum


if __name__ == '__main__':
    serial_number = 1788

    # top left is (1,1), top right is (300,1)
    for x in range(1, 301 - 3):
        for y in range(1, 301 - 3):
            # this x, y represents the top left corner of a 3x3 grid
            POWER_MAP[(x, y)] = calculate_grid_power_level(x, y, serial_number)

    print(sorted(POWER_MAP.items(), key=lambda val: val[1], reverse=True)[:5])
