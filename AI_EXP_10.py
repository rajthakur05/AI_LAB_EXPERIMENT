
from itertools import permutations

def travelling_salesman(graph, start):
    n = len(graph)
    cities = list(range(n))
    cities.remove(start)

    min_cost = float('inf')
    best_path = None

    for perm in permutations(cities):
        current_cost = 0
        current_path = [start]
        k = start

        for city in perm:
            current_cost += graph[k][city]
            current_path.append(city)
            k = city

        current_cost += graph[k][start]
        current_path.append(start)

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path

    return best_path, min_cost


n = int(input("Enter the number of cities: "))

graph = []

print("Enter the adjacency matrix (space-separated values):")
for i in range(n):
    row = list(map(int, input().split()))

    if len(row) != n:
        print("Error: Each row must contain exactly", n, "values.")
        exit()

    graph.append(row)

start = int(input(f"Enter the starting city (0 to {n - 1}): "))

if start < 0 or start >= n:
    print("Error: Invalid starting city.")
else:
    best_path, min_cost = travelling_salesman(graph, start)

    print("\nBest path:", " -> ".join(map(str, best_path)))
    print("Minimum cost:", min_cost)



#input
"""Enter the number of cities: 4
Enter the adjacency matrix (space-separated values):
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
Enter the starting city (0 to 3): 0"""

#output
""" Best path: 0 -> 1 -> 3 -> 2 -> 0
Minimum cost: 80"""