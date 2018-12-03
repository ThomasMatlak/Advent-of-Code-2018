from collections import defaultdict
import re

def main():
    with open("input.txt", "r") as inputfile:
        lines = inputfile.readlines()

        fabric = defaultdict(lambda: defaultdict(int))

        count_overlap = 0

        pattern = re.compile(r"#\d+ @ (\d+),(\d+): (\d+)x(\d+)")

        for line in lines:
            line_components = pattern.split(line)
            start_x = int(line_components[1])
            start_y = int(line_components[2])

            for x in range(int(line_components[3])):
                for y in range(int(line_components[4])):
                    fabric[start_x + x][start_y + y] += 1
                    if fabric[start_x + x][start_y + y] == 2:
                        count_overlap += 1

        print(count_overlap)

if __name__ == "__main__":
    main()
