import heapq

arr = [5,6,7,8,9]

def k_closest_number(arr, x, k):
    heap = []
    result = []
    for e in arr:
        heapq.heappush(heap, (abs(e-x), e))
        breakpoint()
        if len(heap) > k:
            heapq.heappop(heap)
    while heap:
        result.append(heapq.heappop(heap)[1])
    return result    


       


print(k_closest_number(arr, 7,3))





