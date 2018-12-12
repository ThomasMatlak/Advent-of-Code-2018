def main():
    grid_serial_number = 7803

    grid = [[0 for x in range(300)] for y in range(300)]
    is_set = [[False for _ in range(300)] for _ in range(300)]

    max_power = -100000000
    max_power_cell = (0,0)

    for x in range(300 - 3):
        for y in range(300 - 3):
            cell_power = 0

            for x_sub in range(3):
                for y_sub in range(3):
                    if is_set[x + x_sub][y + y_sub]:
                        cell_power += grid[x + x_sub][y + y_sub]
                    else:
                        rack_id = x + x_sub + 10
                        power = rack_id * (y + y_sub)
                        power += grid_serial_number
                        power *= rack_id
                        power = int("{0:03d}".format(power)[-3])
                        power -= 5
                        
                        cell_power += power
                        grid[x + x_sub][y + y_sub] = power
                        is_set[x + x_sub][y + y_sub] = True

            if cell_power > max_power:
                max_power = cell_power
                max_power_cell = (x, y)

    print("{},{}".format(max_power_cell[0], max_power_cell[1]))

if __name__ == "__main__":
    main()
