import timeit
import cProfile

def sub_function(n):
#sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
    
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
# third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]


cProfile.run("test_function()")
print("-"*80)
cProfile.run("third_function()")


# 1. A profiler is tool used for analyzing the performance of a program while it is executed. It measures various aspects such as execution time and memory usage which can be further used for optimizing the code for better efficiency.
# 2. Benchmarking is a coarse-grained measurement, whereas profiling is fine-grained. Benchmarking measures the abolute performance of a software on a particular platform, but profiling measures the relative system statistics.
# 4.
