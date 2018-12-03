from collections import defaultdict
import re

def main():
    with open("input.txt", "r") as inputfile:
        lines = inputfile.readlines()

        fabric = defaultdict(lambda: defaultdict(list))
        ids = defaultdict(bool)

        pattern = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")

        for line in lines:
            line_components = pattern.split(line)

            id = line_components[1]
            if not id in ids:
                ids[id] = False

            start_x = int(line_components[2])
            start_y = int(line_components[3])

            for x in range(int(line_components[4])):
                for y in range(int(line_components[5])):
                    fabric[start_x + x][start_y + y].append(id)

                    if len(fabric[start_x + x][start_y + y]) > 1:
                        for i in fabric[start_x + x][start_y + y]:
                            ids[i] = True

        for id in ids:
            if not ids[id]:
                print(id)

if __name__ == "__main__":
    main()
