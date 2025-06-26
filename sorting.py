import random, timeit

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        arr[k:] = L[i:] + R[j:]

setup_code = '''
from __main__ import insertion_sort, merge_sort
import random
small = [random.randint(0, 1000) for _ in range(100)]
medium = [random.randint(0, 10000) for _ in range(1000)]
large = [random.randint(0, 100000) for _ in range(10000)]
'''


print("Інсерція (1000):", timeit.timeit("insertion_sort(small[:])", setup=setup_code, number=1))
print("Злиття (1000):", timeit.timeit("merge_sort(small[:])", setup=setup_code, number=1))
print("Timsort:", timeit.timeit("sorted(small[:])", setup=setup_code, number=1))

print("Інсерція (10000):", timeit.timeit("insertion_sort(medium[:])", setup=setup_code, number=1))
print("Злиття (10000):", timeit.timeit("merge_sort(medium[:])", setup=setup_code, number=1))
print("Timsort:", timeit.timeit("sorted(medium[:])", setup=setup_code, number=1))

print("Інсерція (1000):", timeit.timeit("insertion_sort(large[:])", setup=setup_code, number=1))
print("Злиття (1000):", timeit.timeit("merge_sort(large[:])", setup=setup_code, number=1))
print("Timsort:", timeit.timeit("sorted(large[:])", setup=setup_code, number=1))