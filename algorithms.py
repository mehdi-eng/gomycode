# Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Calculate the value of 'a' to the power 'b'
def power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

# Bubble Sort Algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Merge Sort Algorithm
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Quick Sort Algorithm
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Test the functions
arr1 = [1, 2, 3, 5, 8]
print(binary_search(arr1, 6))  # Binary Search - Output: False
print(binary_search(arr1, 5))  # Binary Search - Output: True

print(power(3, 4))  # Power Calculation - Output: 81

sample_data = [29, 13, 22, 37, 52, 49, 46, 71, 56]

bubble_sort(sample_data)
print(sample_data)  # Bubble Sort - Output: [13, 22, 29, 37, 46, 49, 52, 56, 71]

sample_data = [29, 13, 22, 37, 52, 49, 46, 71, 56]
merge_sort(sample_data)
print(sample_data)  # Merge Sort - Output: [13, 22, 29, 37, 46, 49, 52, 56, 71]

sample_data = [29, 13, 22, 37, 52, 49, 46, 71, 56]
sorted_data = quick_sort(sample_data)
print(sorted_data)  # Quick Sort - Output: [13, 22, 29, 37, 46, 49, 52, 56, 71]
