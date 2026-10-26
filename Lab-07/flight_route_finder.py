
flights = {
    "Islamabad": [("Lahore", 40), ("Karachi", 90)],
    "Lahore": [("Karachi", 50), ("Peshawar", 30)],
    "Karachi": [("Quetta", 60)],
    "Peshawar": [("Quetta", 70)],
    "Quetta": []
}

def ucs(graph, start, goal):
    queue = [(0, [start])]
    visited = []
    explored = 0

    while queue:
        queue.sort()
        cost, path = queue.pop(0)
        city = path[-1]

        if city in visited:
            continue

        visited.append(city)
        explored += 1

        if city == goal:
            print("Total routes explored:", explored)
            return path, cost

        for next_city, price in graph[city]:
            if next_city not in visited:
                queue.append((cost + price, path + [next_city]))

    print("Total routes explored:", explored)
    return None, None

route, cost = ucs(flights, "Islamabad", "Quetta")

print("Cheapest route:", route)
print("Total cost:", cost)

# Updated from cloned folder