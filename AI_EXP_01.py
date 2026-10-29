from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    print("BFS Traversal:", end=" ")

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Create graph
graph = {}

n = int(input("Enter the number of vertices: "))

for i in range(n):
    vertex = input(f"Enter vertex {i + 1}: ")
    neighbors = input(
        f"Enter adjacent vertices of {vertex} (space-separated): "
    ).split()
    graph[vertex] = neighbors

# Input starting vertex after graph is created
start = input("Enter the starting vertex: ")

print("\nGraph:", graph)

# Check if start vertex exists
if start in graph:
    bfs(graph, start)
else:
    print("Starting vertex not found in the graph.")



#OUTPUT
'''Enter the number of vertices: 10
Enter vertex 1: A
Enter adjacent vertices of A (space-separated): B C
Enter vertex 2: B
Enter adjacent vertices of B (space-separated): D E
Enter vertex 3: C
Enter adjacent vertices of C (space-separated): F G
Enter vertex 4: D
Enter adjacent vertices of D (space-separated): H
Enter vertex 5: E
Enter adjacent vertices of E (space-separated): I
Enter vertex 6: F
Enter adjacent vertices of F (space-separated): J
Enter vertex 7: G
Enter adjacent vertices of G (space-separated): 
Enter vertex 8: H
Enter adjacent vertices of H (space-separated): 
Enter vertex 9: I
Enter adjacent vertices of I (space-separated): 
Enter vertex 10: J
Enter adjacent vertices of J (space-separated): 
Enter the starting vertex: A

Graph: {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': ['H'], 'E': ['I'], 'F': ['J'], 'G': [], 'H': [], 'I': [], 'J': []}
BFS Traversal: A B C D E F G H I J '''