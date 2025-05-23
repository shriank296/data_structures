from collections import defaultdict

edges = [(1,2),(2,3),(3,4),(4,2),(1,3)]

graph = defaultdict(list)

for i,j in edges:
    graph[i].append(j)
    graph[j].append(i)

print(graph)    