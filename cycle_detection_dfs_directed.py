def cycle_detection_directed_dfs(adj_list, source, visited = set(), current_path = set()):
    visited.add(source)
    current_path.add(source)
    print(source)
    for neighbour in adj_list[source]:
        if neighbour not in visited:
            if cycle_detection_directed_dfs(adj_list, neighbour, visited, current_path):
                return True
        else:
            if neighbour in current_path:
                return True
    current_path.remove(source)
    return False        
        

adjacency_list = {1: [2], 2: [6,3], 3: [4], 4: [5], 5: [2], 6:[]}        


print(cycle_detection_directed_dfs(adjacency_list, 1))
            

