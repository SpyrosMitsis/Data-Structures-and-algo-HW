from time import time, sleep
import random
import numpy as np
import matplotlib.pyplot as plt

def bubble_sort(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                
    return data

def partition(data, lo, hi):
    pivot = data[hi]

    i = lo - 1
    for j in range(lo, hi):
        if data[j] < pivot:
            i  = i + 1
            data[i], data[j] = data[j], data[i]

    data[i + 1], data[hi] = data[hi], data[i + 1]
            
    return i + 1

    
def quick_sort(data, lo, hi):
    if lo <= hi:

        pivot = partition(data, lo, hi)

        quick_sort(data, lo, pivot - 1)
        quick_sort(data, pivot + 1, hi)


def find_even_numbers(data):
    counter = 0
    for i in data:
        if i % 2 == 0:
            counter += 1
    return counter



bubble_time_complexity = []
quick_time_complexity = []
even_numbers_complexity = []
values = []
for i in range(100, 40000, 100):
    values.append(i)

for n in values:
    data = [random.randint(1, 1000) for i in range(n)]
    # start_time = time()
    # bubble_sort(data)
    # end_time = time()
    # print("bubble sort", end= " ")
    # print(end_time - start_time)
    # bubble_time_complexity.append(end_time - start_time)

    start_time = time()
    quick_sort(data, 0, n - 1)
    end_time = time()

    quick_time_complexity.append(end_time - start_time)
    print("quick sort ", end= " ")
    print(end_time - start_time)
    print()

    # start_time = time()
    # find_even_numbers(data)
    # end_time = time()
    # print(end_time - start_time)
    # even_numbers_complexity.append(end_time - start_time)
# 
plt.scatter(values, bubble_time_complexity, label="bubble sort")
plt.scatter(values, quick_time_complexity, label='quick sort')
# plt.scatter(values, even_numbers_complexity, label='even number')


plt.grid(True)
plt.legend()
plt.show()
