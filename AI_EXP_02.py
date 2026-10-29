def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


graph = {}

n = int(input("Enter the number of vertices: "))

for i in range(n):
    vertex = input(f"Enter vertex {i+1}: ")
    neighbors = input(f"Enter adjacent vertices of {vertex} (space-separated): ").split()
    graph[vertex] = neighbors   # Store in dictionary

start = input("Enter the starting vertex: ")

print("\nGraph:", graph)
print("DFS Traversal:", end=" ")

visited = set()
dfs(graph, start, visited)



#output

'''
Enter the number of vertices: 10
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
DFS Traversal: A B D H E I C F J G 
'''