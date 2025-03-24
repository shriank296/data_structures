import heapq

heap = []

arr = [2,4,10,7,15,18]

def k_largest(arr, k):
    for element in arr:
        heapq.heappush(heap, element)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap

print(k_largest(arr,3))

