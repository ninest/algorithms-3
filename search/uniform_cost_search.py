import heapq

graph = {
    # node: (node, cost)
    1: [(2, 3), (5, 2), (3, 4)],
    2: [(4, 1), (7, 5)],
    3: [(5, 2), (6, 3)],
    4: [(8, 4)],
    5: [(7, 1)],
    6: [(9, 5)],
    7: [(8, 2), (10, 2)],
    8: [(10, 4)],
    9: [(10, 3)],
    10: [],
}
graph2 = {
    1: [(2, 1), (5, 2)],
    2: [(3, 1)],
    3: [(4, 1)],
    4: [(5, 1)],
    5: [(6, 1)],
    6: [],
}
graph = graph2


def ucs(graph, start, target):
    pqueue = [(0, start)]  # (cost, node)
    visited = set()

    while pqueue:
        cost, node = heapq.heappop(pqueue)

        if node in visited:
            # skip and continue because we have been here
            continue

        if node == target:
            print(f"Found {node} with cost {cost}")
            return

        if node in graph:
            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pqueue, (cost + edge_cost, neighbor))
