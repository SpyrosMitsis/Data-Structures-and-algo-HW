from time import time
import random
import matplotlib.pyplot as plt
import csv

def find_even_numbers(data):
    counter = 0
    for i in data:
        if i % 2 == 0:
            counter += 1
    return counter
            

time_complexity = []
values = [1000, 5000, 10000, 50000, 100000, 500000, 1000000, 2000000, 3000000, 3500000, 4000000, 5000000]

for n in values:
    data = [random.randint(1, 1000) for i in range(n)]
    start_time = time()
    
    print(find_even_numbers(data))
    end_time = time()
    print("number finder", end_time - start_time)
    time_complexity.append(end_time - start_time)

print(len(values))
print(len(time_complexity))

def gradient_descent(m_now, b_now, x_data, y_data, L):
    m_gradient = 0
    b_gradient = 0

    n = len(x_data)

    for i in range(n):
        x = x_data[i]
        y = y_data[i]

        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - m_gradient * L
    b = b_now - b_gradient * L

    print("inside the gradient", m, b)
    return m, b

x = []
y = []

with open('linear_dataset.csv', newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
  
    next(reader)
    # Iterate over each row in the CSV file
    for row in reader:
        # Convert the values to float and append to the respective lists
        x.append(float(row[0]))
        y.append(float(row[1]))



m = 0
b = 0
L = 0.0000000000001

epoch = 10000

for i in range(epoch):
     m, b = gradient_descent(m, b, values, time_complexity, L)

print(m, b)

plt.scatter(values, time_complexity, label="time complexity")
plt.plot(values, [m * x + b for x in values], color='red')

plt.grid(True)
plt.legend()
plt.show()