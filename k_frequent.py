from collections import Counter
import heapq

seq = [1,1,1,3,2,2,4]

def k_frequent_numbers_using_hash_and_sortin(arr, k):
    counter = Counter(arr)
    sorted_counter = sorted(counter.items(), key=lambda x : x[1], reverse=True)
    return [i[0] for i in sorted_counter[:k]]


def k_frequent_numbers_hash(arr, k):
    counter = Counter(arr)
    heap = []
    result = []
    for key, value in counter.items():
        heapq.heappush(heap, (value,key))
        if len(heap) > k:
            heapq.heappop(heap)
    while heap:
        result.append(heapq.heappop(heap)[1])
    return result


print(k_frequent_numbers_hash(seq,2))





