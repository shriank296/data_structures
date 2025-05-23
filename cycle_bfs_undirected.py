from collections import deque

def cycle_detection_bfs_undirected(adj_list, source):
    visited = {source}
    dq = deque()
    dq.append(source)
    parent = {source: None}
    while dq:
        front = dq.popleft()
        for neighbour in adj_list[front]:
            if neighbour not in visited:
                visited.add(neighbour)
                dq.append(neighbour)
                parent[neighbour] = front
            else:
                if parent[front] != neighbour:
                    return True  
    return False                 


adc_list = {"A": ["B"], "B": ["C", "D", "E", "A"], "C": ["B"], "D":["B","F"],"E":["B", "F"], "F": ["D","E"]}
print(cycle_detection_bfs_undirected(adc_list, 'A'))