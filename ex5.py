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
        target = random.choice(arr)
        t = timeit.timeit(lambda: search_func(arr, target), number=iterations)
        total_time += t
    avg_total_time = total_time / trials
    return avg_total_time / iterations


sizes = [1000, 2000, 4000, 8000, 16000, 32000]
linear_times = []
binary_times = []

for i in sizes:
    arr = list(range(i))
    li_time = measure_search_time(linear_search, arr)
    bi_time = measure_search_time(binary_search, arr)
    linear_times.append(li_time)
    binary_times.append(bi_time)
    
    print(f'Size: {size}, Linear Search Avg Time: {li_time:.10e}, Binary Search Avg Time: {bi_time:.10e}')

def linear_fit(n, a, b):
    return a * n + b

def log_fit(n, a, b):
    return a * np.log(n) + b

li_params, _ = curve_fit(linear_fit, sizes, linear_times)
bi_params, _ = curve_fit(log_fit, sizes, binary_times)

# Generate fitted values
fit_linear = linear_fit(np.array(sizes), *lin_params)
fit_binary = log_fit(np.array(sizes), *bin_params)

plt.figure(figsize=(10, 10))
plt.plot(sizes, linear_times, label="Linear Search Times")
plt.plot(sizes, fit_linear, label="Linear Fit")

plt.plot(sizes, binary_times, label="Binary Search Times")
plt.plot(sizes, fit_binary, label="Log Fit")

plt.xlabel("Array Size")
plt.ylabel("Average Time")
plt.legend()
plt.title("Search Algorithm Performance")
plt.show()

# Discussion in comments
"""
1. Linear Search: The function has O(n) complexity.
   Parameters: a = {lin_params[0]}, b = {lin_params[1]}

2. Binary Search: The function has O(log n) complexity.
   Parameters: a = {bin_params[0]}, b = {bin_params[1]}

The results match our expectation as binary search is much more efficient than linear search. 
"""
