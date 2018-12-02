from collections import defaultdict

def main():
    with open("input.txt", "r") as inputfile:
        lines = inputfile.readlines()

        exactly_two_of_a_letter = 0
        exactly_three_of_a_letter = 0

        for line in lines:
            letter_counts = defaultdict(int)
            for char in line:
                letter_counts[char] = letter_counts[char] + 1
            if 2 in letter_counts.values():
                exactly_two_of_a_letter = exactly_two_of_a_letter + 1
            if 3 in letter_counts.values():
                exactly_three_of_a_letter = exactly_three_of_a_letter + 1

        print(exactly_two_of_a_letter * exactly_three_of_a_letter)

if __name__ == "__main__":
    main()
