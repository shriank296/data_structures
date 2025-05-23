def if_path_exists(adjacency_list, source,destination, visited = set()):
    visited.add(source)
    print(source)
    for neighbour in adjacency_list[source]:
        if neighbour not in visited:
            if_path_exists(adjacency_list, neighbour, destination, visited)
    return destination in visited


adjacency_list = {0:[1,2], 1: [0], 2: [0,3], 3:[2],4: [5], 5: [4,6], 6:[5]}

print(if_path_exists(adjacency_list, 0,4))
   

