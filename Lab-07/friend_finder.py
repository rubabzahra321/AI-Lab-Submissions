
graph = {
    "Ali": ["Bilal", "Sara"],
    "Bilal": ["Ali", "Zara"],
    "Sara": ["Ali", "Omar"],
    "Zara": ["Bilal", "Hira"],
    "Omar": ["Sara"],
    "Hira": ["Zara"],
    "Rubab": ["Sara", "Hira"]
}

def bfs(graph, start, goal):
    queue = [[start]]
    visited = [start]

    while queue:
        path = queue.pop(0)
        person = path[-1]

        if person == goal:
            return path

        for friend in graph[person]:
            if friend not in visited:
                visited.append(friend)
                queue.append(path + [friend])

    return None

print(bfs(graph, "Ali", "Hira"))

# Updated from cloned folder