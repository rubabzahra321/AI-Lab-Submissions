maze = {
    "Entrance": ["Hall1", "Hall2"],
    "Hall1": ["Room1"],
    "Hall2": ["Room2", "Trap"],
    "Room1": [],
    "Room2": ["Exit"],
    "Trap": [],
    "Exit": [],
    "HiddenRoom": []
}

def dfs_can_reach(maze, start, exit_room):
    stack = [start]
    visited = []

    while stack:
        room = stack.pop()

        if room not in visited:
            visited.append(room)

            if room == exit_room:
                break

            for next_room in maze[room]:
                stack.append(next_room)

    print("Rooms visited:", visited)
    return exit_room in visited

print("Can reach Exit:", dfs_can_reach(maze, "Entrance", "Exit"))