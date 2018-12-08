from collections import defaultdict
import re

def find_closest_coord(point: tuple, points_cmp: list) -> list:
    min_distance = 10000000000 # just needs to be high enough
    closest_points = None

    x = point[0]
    y = point[1]

    for comp_point in points_cmp:
        x_cmp = comp_point[0]
        y_cmp = comp_point[1]

        dist = abs(x - x_cmp) + abs(y - y_cmp)

        if dist < min_distance:
            min_distance = dist
            closest_points = [(x_cmp, y_cmp)]
        elif dist == min_distance:
            closest_points.append((x_cmp, y_cmp))

    return closest_points

def check_if_coordinate_area_is_infinite(coord: tuple, grid: list) -> bool:
    max_x = len(grid)
    max_y = len(grid[0])

    for i in range(max_x):
        if grid[i][0] == coord or grid[i][max_y - 1] == coord:
            return True
    for i in range(max_y):
        if grid[0][i] == coord or grid[max_x - 1][i] == coord:
            return True
    return False

def main() -> None:
    with open("input.txt", "r") as inputfile:
        lines = inputfile.read().splitlines()

        max_x = 0
        max_y = 0

        coordinates = []

        for line in lines:
            m = re.match(r"(\d+), (\d+)", line)
            coord = m.group(1, 2)
            coord = (int(coord[0]), int(coord[1]))
            coordinates.append(coord)

            if coord[0] > max_x:
                max_x = coord[0]
            if coord[1] > max_y:
                max_y = coord[1]

        grid = [["." for _ in range(max_y + 1)] for _ in range(max_x + 1)]

        for coord in coordinates:
            grid[coord[0]][coord[1]] = coord

        # find the closest coordinate for each spot in the grid
        for x in range(max_x):
            for y in range(max_y):
                if grid[x][y] == ".":
                    closets_coord = find_closest_coord((x, y), coordinates)
                    if len(closets_coord) == 1:
                        grid[x][y] = closets_coord[0]

        # count areas
        areas = defaultdict(int)
        for coord in coordinates:
            # check it is not on the edge of the grid -> this implies the area is infinite and we only want bounded areas
            if check_if_coordinate_area_is_infinite(coord, grid):
                continue
            for x in range(max_x):
                for y in range(max_y):
                    if grid[x][y] == coord:
                        areas[coord] += 1

        # get the largest area
        print(max(areas.items(), key=lambda a: a[1]))

if __name__ == "__main__":
    main()
