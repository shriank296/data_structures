from collections import deque

def breadth_first_search(adjacency_list: dict[int, list[int]], source_node: int):
    dq = deque()
    dq.append(source_node)
    visited = {source_node}
    while dq:
        out = dq.popleft()
        print(out, end= " ")
        for node in adjacency_list[out]:
            if node not in visited:
                dq.append(node)
                visited.add(node)
    print()

if __name__ == "__main__":
    adjacency_list = {0:[1,5,2], 2: [0,3], 3: [2,4], 4: [3], 1: [0], 5: [0]}
breadth_first_search(adjacency_list, 0)





