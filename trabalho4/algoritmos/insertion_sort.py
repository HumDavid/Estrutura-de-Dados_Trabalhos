def insertion_sort(arr):
    comp = 0
    swaps = 0
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comp += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
        
        if j != i - 1:
            arr[j + 1] = key
    
    return comp, swaps