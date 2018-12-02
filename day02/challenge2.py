def main():
    with open("input.txt", 'r') as inputfile:
        lines = inputfile.readlines()

        for x in lines:
            for y in lines:
                if x == y:
                    continue
                diff_positions = []
                for i in range(len(x)):
                    if not x[i] == y[i]:
                        diff_positions.append(i)
                if len(diff_positions) == 1:
                    print(x[:diff_positions[0]] + x[diff_positions[0] + 1:])

if __name__ == "__main__":
    main()
