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
    with open("input.txt", "r") as inputfile:
        lines = inputfile.readlines()

        for line in lines:
            polymer = line[:-1]
            # get a list of all unit types
            unit_types = []
            for c in polymer:
                if not c.lower() in unit_types:
                    unit_types.append(c)

            # try removing each unit type from the polymer and running the reaction
            results = {}
            for unit_type in unit_types:
                modified_polymer = ""
                for c in polymer:
                    if c.lower() != unit_type:
                        modified_polymer += c
                results[unit_type] = len(react(modified_polymer))

            print(min(results.items(), key=lambda a: a[1])[1])

if __name__ == "__main__":
    main()
