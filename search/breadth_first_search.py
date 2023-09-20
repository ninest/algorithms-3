from queue import Queue


def breadth_first_search(graph: dict, start: str) -> "list[str]":
    explored = set(start)
    result = [start]
    queue = Queue()
    queue.put(start)

    while not queue.empty():
        next_node = queue.get()
        for neighbor in graph[next_node]:
            if neighbor not in explored:
                explored.add(neighbor)
                result.append(neighbor)
                queue.put(neighbor)

    return result


def breadth_first_search_path(graph: dict, start: str, target: str) -> "list[str]":
    # node, path
    queue = Queue()
    queue.put((start, [start]))

    while not queue.empty():
        next_node, path = queue.get()

        if next_node == target:
            return path

        for neighbor in graph[next_node]:
            if neighbor not in path:
                new_path = path + [neighbor]
                queue.put((neighbor, new_path))

    return []


if __name__ == "__main__":
    G = {
        "A": ["B", "C", "D"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B", "D"],
        "E": ["B", "F"],
        "F": ["C", "E", "G"],
        "G": ["F"],
    }

    # print(breadth_first_search(G, "A"))
    print(breadth_first_search_path(G, "A", "G"))
