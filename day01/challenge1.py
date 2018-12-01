def main():
    sum = 0

    with open("input.txt", "r") as inputfile:
        lines = inputfile.readlines()

        for line in lines:
            num = int(line[1:])
            if line[0] == "+":
                sum = sum + num
            elif line[0] == "-":
                sum = sum - num
    print(sum)

if __name__ == "__main__":
    main()
