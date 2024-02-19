from time import time
import random
import matplotlib.pyplot as plt
from typing import  List
from scipy.optimize import curve_fit

def find_even_numbers(data: List[int]) -> int:
    counter = 0
    for i in data:
        if i % 2 == 0:
            counter += 1
    return counter
            

time_complexity = []
values = [1000, 5000, 10000, 50000, 100000, 500000, 1000000, 2000000,  3000000, 5000000]

for n in values:
    data = [random.randint(1, 1000) for i in range(n)]
    start_time = time()
    
    print(find_even_numbers(data))
    end_time = time()
    print("number finder", end_time - start_time)
    time_complexity.append(end_time - start_time)

plt.plot(values, time_complexity, label="time complexity")
plt.grid(True)
plt.legend()
plt.show()

