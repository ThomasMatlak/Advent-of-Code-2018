# Inital thought was to use a recursive approach. This works, but on the puzzle input this quickly reached a stack overflow
def react_recursive(polymer: str) -> str:
    output = ""

    for i in range(len(polymer)):
        if i == len(polymer) - 1:
            output += polymer[i]
        elif ((polymer[i].islower() and polymer[i + 1].isupper()) or (polymer[i].isupper() and polymer[i + 1].islower())) and polymer[i].lower() == polymer[i+1].lower():
            return react_recursive(polymer[:i] + polymer[i + 1 + 1:])
        else:
            output += polymer[i]

    return output

def react(polymer: str) -> str:
    current_polymer = polymer
    output = None

    while True:
        output = ""
        reaction_occurred = False

        i = 0
        while i < len(current_polymer):
            indexes = []

            if i == len(current_polymer) - 1:
                output += current_polymer[i]
            elif ((current_polymer[i].islower() and current_polymer[i + 1].isupper()) or (current_polymer[i].isupper() and current_polymer[i + 1].islower())) and current_polymer[i].lower() == current_polymer[i + 1].lower():
                indexes.append(i)
                indexes.append(i + 1)
                reaction_occurred = True
                i += 1
            else:
                output += polymer[i]

            num_removed = 0
            for idx in indexes:
                current_polymer = current_polymer[:idx - num_removed] + current_polymer[idx - num_removed + 1:]
                num_removed += 1
            i += 1

        if not reaction_occurred:
            break

    return output

def main() -> None:
#     input = "dabAcCaCBAcCcaDA"
#     print(react_recursive(input))
#     print(len(react_recursive(input)))

#     input = "dabAcCaCBAcCcaDA"
#     print(react(input))
#     print(len(react(input)))

    with open("input.txt", "r") as inputfile:
        lines = inputfile.readlines()

        units = 0

        for line in lines:
            fully_reacted_polymer = react(line[:-1])
            units += len(fully_reacted_polymer)
        print(units)

if __name__ == "__main__":
    main()
