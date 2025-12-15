from algoritmos.insertion_sort import insertion_sort
from algoritmos.selection_sort import selection_sort
from algoritmos.bubble_sort import bubble_sort
from algoritmos.shell_sort import shell_sort
from algoritmos.merge_sort import merge_sort
from algoritmos.quick_sort import quick_sort
from algoritmos.heap_sort import heap_sort
from algoritmos.counting_sort import counting_sort

def testing_algorithms():
    original_list = [
        12, 42, 83, 25, 67, 71, 3, 4, 94, 53,
        100, 48, 19, 61, 86, 33, 13, 43, 84, 28,
        81, 60, 6, 49, 40, 41, 38, 64, 44, 36,
        45, 27, 11, 89, 63, 39, 9, 58, 52, 17,
        88, 77, 26, 62, 30, 96, 56, 65, 98, 99,
        76, 73, 16, 95, 35, 87, 68, 69, 51, 92,
        37, 75, 90, 82, 8, 18, 23, 93, 57, 10,
        15, 97, 14, 29, 7, 24, 31, 59, 78, 85,
        5, 70, 55, 91, 47, 72, 2, 20, 34, 74,
        50, 66, 32, 22, 54, 79, 21, 1, 80, 46
    ]
    
    algorithms = [
        ("Insertion Sort", insertion_sort),
        ("Selection Sort", selection_sort),
        ("Bubble Sort", bubble_sort),
        ("Shell Sort", shell_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort),
        ("Counting Sort", counting_sort)
    ]
    
    print("=" * 70)
    print("="*23 + " ALGORITMOS DE ORDENAÇÃO " + "="*22)
    print("=" * 70 + "\n")
    
    results = []
    
    for name, algorithm in algorithms:
        arr_copy = original_list.copy()
        
        print(f"{name}:")
        print(f"  Lista antes: {arr_copy[:10]}...")
        
        comp, swaps = algorithm(arr_copy)
        
        print(f"  Lista após: {arr_copy[:10]}...")
        print(f"  Comparações: {comp}")
        print(f"  Trocas: {swaps}")
        print()
        
        results.append((name, comp, swaps))

if __name__ == "__main__":
    testing_algorithms()