
warehouse = {
    "Receiving": {"Aisle1": 40, "Aisle2": 70},
    "Aisle1": {"Aisle2": 30, "Packing Station": 90},
    "Aisle2": {"Packing Station": 35},
    "Packing Station": {}
}

heuristic = {
    "Receiving": 100,
    "Aisle1": 70,
    "Aisle2": 35,
    "Packing Station": 0
}


def get_g(path):
    total = 0

    for i in range(len(path) - 1):
        current = path[i]
        next_node = path[i + 1]
        total = total + warehouse[current][next_node]

    return total


def get_h(path):
    last_node = path[-1]
    return heuristic[last_node]


def get_f(path):
    return get_g(path) + get_h(path)


def a_star(start, goal):
    frontier = [[start]]
    explored = 0

    while len(frontier) > 0:
        frontier.sort(key=get_f)

        path = frontier.pop(0)
        node = path[-1]

        explored = explored + 1

        print("Exploring:", node,
              "g =", get_g(path),
              "h =", get_h(path),
              "f =", get_f(path))

        if node == goal:
            print("\nPath found by A*:", path)
            print("Total cost of this path:", get_g(path))
            print("Total nodes explored:", explored)
            return path

        for neighbour in warehouse[node]:
            new_path = path + [neighbour]
            frontier.append(new_path)

    return None



result = a_star("Receiving", "Packing Station")


print("\n--- Final Result ---")
print("Starting Location: Receiving")
print("Goal Location: Packing Station")
print("Final Path:", result)

if result is not None:
    print("Final Path Cost:", get_g(result))
else:
    print("No path found!")

# THIS IS TESTING PURPOSES ONLY. DO NOT MODIFY THIS CODE.