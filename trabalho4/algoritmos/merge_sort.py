def merge_sort(arr):
    def merge_sort_helper(arr, left, right, comp, swaps):
        if left < right:
            mid = (left + right) // 2
            
            comp1, swaps1 = merge_sort_helper(arr, left, mid, comp, swaps)
            comp2, swaps2 = merge_sort_helper(arr, mid + 1, right, comp, swaps)
            
            comp3, swaps3 = merge(arr, left, mid, right)
            
            return comp + comp1 + comp2 + comp3, swaps + swaps1 + swaps2 + swaps3
        return 0, 0
    
    def merge(arr, left, mid, right):
        comp = 0
        swaps = 0
        
        n1 = mid - left + 1
        n2 = right - mid
        
        L = arr[left:mid + 1]
        R = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < n1 and j < n2:
            comp += 1
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                swaps += 1
                j += 1
            k += 1
        
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
        
        return comp, swaps
    
    comp, swaps = merge_sort_helper(arr, 0, len(arr) - 1, 0, 0)
    return comp, swaps