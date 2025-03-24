def sort_recursive(arr):
    if not arr:
        return arr
    temp = arr.pop()
    sorted_arr = sort_recursive(arr)
    insert(sorted_arr, temp)
    return sorted_arr

def insert(seq, temp):
    if not seq or seq[-1] <= temp:
        return seq.append(temp)
    val = seq.pop()
    insert(seq, temp)
    seq.append(val)

print(sort_recursive([5,0,2,3]))
