def counting_sort(arr):
    comp = 0
    swaps = 0
    
    if len(arr) == 0:
        return comp, swaps
    
    max_val = max(arr)
    min_val = min(arr)
    
    count_size = max_val - min_val + 1
    count = [0] * count_size
    
    for num in arr:
        count[num - min_val] += 1
    
    idx = 0
    for i in range(count_size):
        while count[i] > 0:
            arr[idx] = i + min_val
            idx += 1
            count[i] -= 1
            comp += 1
    
    return comp, swaps