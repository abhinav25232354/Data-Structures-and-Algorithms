def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        
        # Merge the two halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # Checking if any element left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    def _quick_sort(items, low, high):
        if low < high:
            pi = partition(items, low, high)
            _quick_sort(items, low, pi - 1)
            _quick_sort(items, pi + 1, high)

    def partition(items, low, high):
        pivot = items[high]
        i = low - 1
        for j in range(low, high):
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1
    
    _quick_sort(arr, 0, len(arr) - 1)

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1   # left
        r = 2 * i + 2   # right

        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    # Build max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

def counting_sort(arr):
    if not arr:
        return
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Store count of each element
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1
    
    # Change count[i] so that count[i] now contains actual position
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    # Build output array
    for i in range(len(arr)-1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    # Copy to original array
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    def counting_sort_exp(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        
        # Count occurrences for digits
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1
        
        for i in range(1, 10):
            count[i] += count[i-1]
        
        for i in range(n-1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
        
        for i in range(n):
            arr[i] = output[i]

    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_exp(arr, exp)
        exp *= 10

# ----------------- Test all --------------------

def test_sort_algorithm(sort_fn, arr):
    test_arr = arr.copy()
    sort_fn(test_arr)
    print(f"{sort_fn.__name__}: {test_arr}")

if __name__ == "__main__":
    sample_arr = [64, 34, 25, 12, 22, 11, 90]

    test_sort_algorithm(bubble_sort, sample_arr)
    test_sort_algorithm(selection_sort, sample_arr)
    test_sort_algorithm(insertion_sort, sample_arr)
    test_sort_algorithm(merge_sort, sample_arr)
    test_sort_algorithm(quick_sort, sample_arr)
    test_sort_algorithm(heap_sort, sample_arr)
    test_sort_algorithm(counting_sort, sample_arr)
    test_sort_algorithm(radix_sort, [170, 45, 75, 90, 802, 24, 2, 66])  # Radix sort expects non-negative integers
