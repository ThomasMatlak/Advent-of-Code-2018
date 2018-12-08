from collections import defaultdict
import re

def sum_of_distances_to_coordinates(point: tuple, coords: list) -> int:
    x = point[0]
    y = point[1]

    dist_sum = 0
    for coord in coords:
        dist_sum += abs(x - coord[0]) + abs(y - coord[1])

    return dist_sum

def main() -> None:
    with open("input.txt", "r") as inputfile:
        lines = inputfile.read().splitlines()

        coordinates = []

        for line in lines:
            m = re.match(r"(\d+), (\d+)", line)
            coord = m.group(1, 2)
            coord = (int(coord[0]), int(coord[1]))
            coordinates.append(coord)
        
        area = 0
        for x in range(-500, 500):
            for y in range(-500, 500):
                if sum_of_distances_to_coordinates((x, y), coordinates) < 10000:
                    area += 1

        print(area)

if __name__ == "__main__":
    main()
