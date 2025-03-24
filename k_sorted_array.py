import heapq

arr = [6,5,3,2,8,10,9]

def k_sorted_array(arr, k):
    heap = []
    sorted_array = []
    for element in arr:
        heapq.heappush(heap, element)
        if len(heap) > k:
            sorted_array.append(heapq.heappop(heap))
    while heap:
        sorted_array.append(heapq.heappop(heap))
    return sorted_array

# print(k_sorted_array(arr, 3))         


def k_sorted_array_constant_space(arr, k):
    heap = []
    i = 0
    for element in arr:
        heapq.heappush(heap, element)
        if len(heap) > k:
            item = heapq.heappop(heap)
            idx = arr.index(item)
            arr[i], arr[idx] = arr[idx], arr[i]
            i += 1
    while heap:
        arr[i] = heapq.heappop(heap)
        i+=1
    return arr


print(k_sorted_array_constant_space(arr, 3))     

