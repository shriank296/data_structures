import heapq

ropes = [1, 2, 3, 4, 5]

def minimum_cost(ropes):
    pq = []
    cost = 0
    for rope in ropes:
        heapq.heappush(pq, rope)
    while pq:
        sum = 0
        for i in range(2):
            sum += heapq.heappop(pq)
        cost += sum    
        if pq:
            heapq.heappush(pq, sum)
    return cost

print(minimum_cost(ropes))    

