from collections import deque

def level_order_traversal_bfs(adjacency_list, source_node):
    dq = deque()
    dq.append(source_node)
    visited = {source_node}
    level = 0
    output = [(source_node, level)]
    while dq:
        size = len(dq)
        while size > 0:
            front = dq.popleft()
            for neighbour in adjacency_list[front]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dq.append(neighbour)
                    output.append((neighbour, level))
            size -= 1
        level += 1
    return output    

adjacency = {0:[1,3], 1: [0,2], 2: [1,3], 3: [0,2,4], 4: [3]}

print(level_order_traversal_bfs(adjacency, 0))
