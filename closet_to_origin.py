import heapq

points = [(1,3), (-2, 2), (5,8), (0,1)]

def distance_from_origin(a,b):
    return (a**2 + b**2)**(1/2)

def k_closest_to_origin(seq, k):
    pq = []
    result = []
    for point in seq:
        heapq.heappush(pq, (distance_from_origin(point[0], point[1]),point))
        if len(pq) > k:
            heapq.heappop(pq)
    while pq:
        result.append(heapq.heappop(pq)[1])
    return result

print(k_closest_to_origin(points, 2))    


