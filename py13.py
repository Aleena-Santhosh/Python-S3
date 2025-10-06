import numpy as np

numbers = []
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

arr = np.array(numbers)

print("Mean:", arr.mean())
print("Standard Deviation:", arr.std())