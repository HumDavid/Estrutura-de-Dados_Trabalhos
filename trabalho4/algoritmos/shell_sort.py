def shell_sort(arr):
    comp = 0
    swaps = 0
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            while j >= gap:
                comp += 1
                if arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    swaps += 1
                    j -= gap
                else:
                    break
            
            arr[j] = temp
        
        gap //= 2
    
    return comp, swaps