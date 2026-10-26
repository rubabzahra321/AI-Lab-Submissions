
campus = {
    "Hostel": {"Cafeteria": 150, "Admin Block": 300},
    "Cafeteria": {"Academic Block": 200},
    "Admin Block": {"Academic Block": 120},
    "Academic Block": {"Library": 100},
    "Common Room": {"Library": 50},
    "Basement": {"Library": 80},
    "Library": {}
}

heuristic = {
    "Hostel": 350,
    "Cafeteria": 260,
    "Admin Block": 150,
    "Academic Block": 90,
    "Library": 0
}


def get_h(path):
    last_node = path[-1]
    return heuristic[last_node]


def get_cost(path):
    total = 0

    for i in range(len(path) - 1):
        current = path[i]
        next_node = path[i + 1]
        total = total + campus[current][next_node]

    return total


def gbfs(start, goal):
    frontier = [[start]]
    visited = []
    explored = 0

    while len(frontier) > 0:
        frontier.sort(key=get_h)

        path = frontier.pop(0)
        node = path[-1]

        if node in visited:
            continue

        visited.append(node)
        explored = explored + 1

        print("Exploring:", node, "h =", get_h(path))

        if node == goal:
            print("\nPath found by GBFS:", path)
            print("Total cost of this path:", get_cost(path))
            print("Total nodes explored:", explored)
            return path

        for neighbour in campus[node]:
            if neighbour not in visited:
                new_path = path + [neighbour]
                frontier.append(new_path)

    return None


gbfs("Hostel", "Library")
