from collections import defaultdict

NUM_GENERATIONS = 50000000000

def main() -> None:
    with open("input.txt", "r") as inputfile:
        lines = inputfile.read().splitlines()

        current_generation = defaultdict(bool)

        initial_state = lines[0][15:]
        for i in range(len(initial_state)):
            state = initial_state[i]
            if state == "#":
                current_generation[i] = True
            elif state == ".":
                current_generation[i] = False

        spread_patterns = {}

        for line in lines[2:]:
            pattern_str = line[:5]
            outcome_char = line[-1]

            pattern = []
            for char in pattern_str:
                if char == "#":
                    pattern.append(True)
                elif char == ".":
                    pattern.append(False)
            outcome = True if outcome_char == "#" else False
            spread_patterns[tuple(pattern)] = outcome

        for _ in range(1, 113 + 1): # at generation 113 the pattern stabalizes, shifting by one 
            new_generation = defaultdict(bool)

            for current_plant in range(min(current_generation) - 2, max(current_generation) + 2):
                surrounding_pattern = []
                for i in range(-2, 2 + 1):
                    surrounding_pattern.append(current_generation[current_plant + i])
                new_generation[current_plant] = spread_patterns[tuple(surrounding_pattern)]

            current_generation = new_generation

        sum_pot_numbers_with_plants = 0
        offset = NUM_GENERATIONS - 113
        for pot in current_generation:
            if current_generation[pot]:
                sum_pot_numbers_with_plants += pot + offset

        print(sum_pot_numbers_with_plants)

if __name__ == "__main__":
    main()
