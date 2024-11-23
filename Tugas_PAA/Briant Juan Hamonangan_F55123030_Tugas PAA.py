import random
import time

# Generate 100 random integers
X = [random.randint(1, 1000) for _ in range(100)]

#1.Bubble Sort
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

#2.Merge Sort
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array

# Measure execution time
def measure_time(func, data):
    start = time.time()
    sorted_data = func(data)
    end = time.time()
    return end - start, sorted_data

# Perform sorting and measure time
bubble_time, bubble_sorted = measure_time(bubble_sort, X.copy())
merge_time, merge_sorted = measure_time(merge_sort, X.copy())

print(f"Bubble Sort Time: {bubble_time:.6f} seconds")
print(f"Merge Sort Time: {merge_time:.6f} seconds")

#Bubble Sort Time: 0.000311 seconds
#Merge Sort Time: 0.000094 seconds