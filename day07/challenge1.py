def prerequisites_met(node: int, graph: list, visited: list) -> bool:
    for i in range(len(graph)):
        if graph[i][node] and not visited[i]:
            return False
    return True

def graph_traversal(graph: list) -> list:
    visited = [False for _ in range(len(graph))]
    traversal_order = []

    visit_next = []

    # add nodes without deg_in = 0
    transposed_graph = list(map(list, zip(*graph)))
    for i in range(len(transposed_graph)):
        if True not in transposed_graph[i]:
            visit_next.append(i)

    while visit_next:
        current_node = min(visit_next)
        while current_node in visit_next:
            visit_next.remove(current_node)
        
        if visited[current_node]:
            continue
        
        visited[current_node] = True
        traversal_order.append(chr(current_node + 65))

        # check if neighbors are fit to be queued
        for i in range(len(graph[current_node])):
            if not graph[current_node][i]:
                continue
            neighbor = i

            if visited[neighbor]:
                continue
            if prerequisites_met(i, graph, visited):
                visit_next.append(neighbor)

    return traversal_order

def main() -> None:
    NUM_NODES = 26

    with open("input.txt", "r") as inputfile:
        lines = inputfile.readlines()

        graph = [[False for _ in range(NUM_NODES)] for _ in range(NUM_NODES)]

        # build dependency graph
        for line in lines:
            start_node = line[5]
            end_node = line[-13]
            graph[ord(start_node) - 65][ord(end_node) - 65] = True

        order = graph_traversal(graph)
        print(''.join(order))

if __name__ == "__main__":
    main()
