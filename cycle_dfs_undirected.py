def cycle_dfs_undirected(adj_list, source, visited = set(), parent = None):
    visited.add(source)
    for neighbour in adj_list[source]:
        if neighbour not in visited:
            if cycle_dfs_undirected(adj_list, neighbour, visited, source):
                return True
        else:
            if neighbour != parent:
                return True
    return False    
        


adc_list = {"A": ["B"], "B": ["C", "D", "E", "A"], "C": ["B"], "D":["B","F"],"E":["B", "F"], "F": ["D","E"]}
print(cycle_dfs_undirected(adc_list, "A"))