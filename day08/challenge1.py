class Node:
    metadata = None
    num_metadata = 0
    children = None

def parse_to_tree(numbers: list):
    root = Node()
    num_children = numbers[0]
    num_metadata = numbers[1]
    root.num_metadata = num_metadata

    if num_children == 0:
        root.metadata = numbers[2:2 + num_metadata]
        return root, numbers[2 + num_metadata:]
    else:
        root.children = []
        numbers = numbers[2:]
        for _ in range(num_children): 
            child, numbers = parse_to_tree(numbers)
            root.children.append(child)
        root.metadata = numbers[:num_metadata]
        return root, numbers[num_metadata:]

def sum_nested_metadata(root: Node) -> int:
    if root.children == None:
        return sum(root.metadata)
    else:
        metadata_sum = sum(root.metadata)
        for child in root.children:
            metadata_sum += sum_nested_metadata(child)
        return metadata_sum

def main() -> None:
    with open("input.txt", "r") as inputfile:
        lines = inputfile.read().splitlines()

        for line in lines:
            numbers = [int(n) for n in line.split()]

            root, _ = parse_to_tree(numbers)

            print(sum_nested_metadata(root))

if __name__ == "__main__":
    main()
