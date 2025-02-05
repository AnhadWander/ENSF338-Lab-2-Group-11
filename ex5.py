import timeit

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return "Value not in data"
        
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return "Value not in data"   

def measure_search_time(search_func, arr, trials=1000, iterations=100):
    total_time = 0.0
    for _ in range(trials):
        target = 32000
        t = timeit.timeit(lambda: search_func(arr, target), number=iterations)
        total_time += t
    avg_total_time = total_time / trials
    return avg_total_time / iterations


arr = [1000, 2000, 4000, 8000, 16000, 32000]

# Randomly chosen value to find is 32000

print("Linear Search Performance:")
lin_avg_time = measure_search_time(linear_search, arr)
print(f"Array: 32000, Average time per call: {lin_avg_time:.10e} seconds")
    
print("\nBinary Search Performance:")
Bin_avg_time = measure_search_time(binary_search, arr)
print(f"Array: 32000, Average time per call: {Bin_avg_time:.10e} seconds")