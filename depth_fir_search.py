from stack import Stack

def depth_first_search(adjacency_list: dict[int, list[int]], node: int, visited = set()):
    print(node)
    visited.add(node)
    for neighbour in adjacency_list[node]:
        if neighbour not in visited:
            depth_first_search(adjacency_list, neighbour, visited)
                











if __name__ == "__main__":
    adjacency_list = {0:[1,5,2], 2: [0,3], 3: [2,4], 4: [3], 1: [0], 5: [0]}
    depth_first_search(adjacency_list, 0)

    
