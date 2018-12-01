def main():
    sum = 0
    sum_occurrences = {0:True}

    with open("input.txt", "r") as inputfile:
        lines = inputfile.readlines()

        while(True):
            for line in lines:
                num = int(line[1:])
                if line[0] == "+":
                    sum = sum + num
                elif line[0] == "-":
                    sum = sum - num

                if sum in list(sum_occurrences.keys()):
                    print(sum)
                    return
                else:
                    sum_occurrences[sum] = True

if __name__ == "__main__":
    main()
