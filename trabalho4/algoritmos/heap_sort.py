def heap_sort(arr):
    comp = 0
    swaps = 0
    
    def heapify(arr, n, i, comp, swaps):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n:
            comp += 1
            if arr[left] > arr[largest]:
                largest = left
        
        if right < n:
            comp += 1
            if arr[right] > arr[largest]:
                largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            swaps += 1
            comp, swaps = heapify(arr, n, largest, comp, swaps)
        
        return comp, swaps
    
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        comp, swaps = heapify(arr, n, i, comp, swaps)
    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        swaps += 1
        comp, swaps = heapify(arr, i, 0, comp, swaps)
    
    return comp, swaps