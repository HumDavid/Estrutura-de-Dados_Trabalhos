def quick_sort(arr):
    def quick_sort_helper(arr, low, high, comp, swaps):
        if low < high:
            pi, comp_part, swaps_part = partition(arr, low, high, comp, swaps)
            
            comp_left, swaps_left = quick_sort_helper(arr, low, pi - 1, 0, 0)
            comp_right, swaps_right = quick_sort_helper(arr, pi + 1, high, 0, 0)
            
            return (comp_part + comp_left + comp_right, 
                   swaps_part + swaps_left + swaps_right)
        return 0, 0
    
    def partition(arr, low, high, comp, swaps):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            comp += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        
        return i + 1, comp, swaps
    
    comp, swaps = quick_sort_helper(arr, 0, len(arr) - 1, 0, 0)
    return comp, swaps