def depth_first_search(graph: dict, start: str) -> "set[str]":
    explored = set(start)
    stack = [start]

    while stack:
        node = stack.pop()
        explored.add(node)

        for neighbor in reversed(graph[node]):
            if neighbor not in explored:
                stack.append(neighbor)

    return explored


def depth_first_search_path(graph: dict, start: str, target: str) -> "list[str]":
    # node, path
    stack = [(start, [start])]

    while stack:
        node, path = stack.pop()

        if node == target:
            return path

        for neighbor in reversed(graph[node]):
            if neighbor not in path:
                new_path = path + [neighbor]
                stack.append((neighbor, new_path))

    # Not path found
    return []


if __name__ == "__main__":
    G = {
        "A": ["B", "C", "D", "G"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B", "D"],
        "E": ["B", "F"],
        "F": ["C", "E", "G"],
        "G": ["F"],
    }

    print(depth_first_search(G, "A"))
    print(depth_first_search_path(G, "A", "G"))
