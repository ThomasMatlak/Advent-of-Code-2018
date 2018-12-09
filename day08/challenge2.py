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

def get_node_value(root: Node) -> int:
    if root.children == None:
        return sum(root.metadata)
    else:
        value = 0
        for v in root.metadata:
            if v <= len(root.children):
                value += get_node_value(root.children[v - 1])
        return value

def main() -> None:
    with open("input.txt", "r") as inputfile:
        lines = inputfile.read().splitlines()

        for line in lines:
            numbers = [int(n) for n in line.split()]

            root, _ = parse_to_tree(numbers)

            print(get_node_value(root))

if __name__ == "__main__":
    main()
