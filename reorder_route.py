adjacency_list = {0:[1,4], 1:[0,3],3:[1,2],2:[3], 4:[0,5], 5:[4]}

forward_adjacency_list = {0: [1], 1:[3], 4:[5]}

def reorder_count_dfs(forward_adjacency_list, adjacency_list, capital_node,visited =set(), min_reorder = 0):
    visited.add(capital_node)
    for neighbour in adjacency_list[capital_node]:
        if neighbour not in visited:
            if neighbour in forward_adjacency_list.get(capital_node,[]):
                min_reorder += 1
            reorder_count_dfs(forward_adjacency_list,adjacency_list,neighbour, visited,min_reorder)
    return min_reorder


print(reorder_count_dfs(forward_adjacency_list,adjacency_list,0))


