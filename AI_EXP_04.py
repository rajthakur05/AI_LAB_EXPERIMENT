graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 2,
    'G': 0
}

def astar(start, goal):
    open_list = [(start, 0)]   # (node, g_cost)
    came_from = {}
    g_cost = {start: 0}

    while open_list:
        # Select node with minimum f = g + h
        current = min(open_list, key=lambda x: x[1] + heuristic[x[0]])
        current_node = current[0]

        # Remove current node from open list
        open_list.remove(current)

        # Goal reached
        if current_node == goal:
            path = [current_node]
            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)
            path.reverse()
            return path, g_cost[goal]

        # Explore neighbors
        for neighbor, cost in graph[current_node]:
            new_cost = g_cost[current_node] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                came_from[neighbor] = current_node
                open_list.append((neighbor, new_cost))

    return None, float('inf')


start = input("Enter the start node: ").upper()
goal = input("Enter the goal node: ").upper()

if start not in graph or goal not in graph:
    print("Invalid start or goal node.")
else:
    path, cost = astar(start, goal)

    if path:
        print("\nShortest Path:", " -> ".join(path))
        print("Total Cost:", cost)
    else:
        print("Path not found.")



# Output
"""Enter the start node: A
Enter the goal node: G

Shortest Path: A -> B -> D -> G
Total Cost: 6 """