import timeit
import matplotlib.pyplot as plt

# Original version
def func_1(n):
    if n == 0 or n == 1:
        return n
    else:
        return func_1(n-1) + func_1(n-2)

# 1. The given code finds the nth Fibonacci number using recursion.
# 2. No, the given code is an example of a divide-and-conquer algorithm
# 3. The expression for the time complexity of the algorithm is O(2^n)

# version of the code which uses memoization

memory = [0, 1]                                     # a global list with initial length of 2
def func_2(n):                                      # declaring func that takes n as an argument
    if n < len(memory):                             # checking if the argument n is less than the length of the memory array
        return memory[n]                            # if the argumnet n is less than the length of the memory array (i.e 2) then n is less than two, that is either 1 or 0 
    memory.append(func_2(n - 1) + func_2(n - 2))    # storing the added value returned from the recursive call of func
    return memory[n]                                # returning the element at n index in the memory list

# 5. The expression for the time complexity of the algorithm is O(n)

# 6. Timing the original code and the improved version, for all integers between 0 and 35, and ploting the results
time_taken_original = []
time_taken_modified = []

for i in range(36):
    time_original = timeit.timeit(lambda: func_1(i), number=1)
    time_taken_original.append(time_original)

for j in range(36):
    time_modified = timeit.timeit(lambda: func_2(j), number=1)
    time_taken_modified.append(time_modified)

print(time_taken_original)
print('*'*80)
print(time_taken_modified)

plt.figure(figsize=(10,10))
plt.title("Time taken by original function")
plt.plot(range(36), time_taken_original, color='r')
plt.ylabel("Time taken")
plt.xlabel("Inputs")
plt.savefig("ex1.6.1.jpg")

plt.figure(figsize=(10,10))
plt.title("Time taken by modified function")
plt.plot(range(36), time_taken_modified, color='b')
plt.ylabel("Time taken")
plt.xlabel("Inputs")
plt.savefig("ex1.6.2.jpg")

