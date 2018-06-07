import numpy as np

filename = "13.dat"
numbers = np.zeros(50)
with open(filename) as file:
    for line in file:
            for i, key in enumerate(line):
                if key != '\n':
                    numbers[i] += int(key)

print (numbers)
for i in range(49,0,-1):
    numbers[i-1] += int(numbers[i]/10)
    numbers[i] = numbers[i]%10

print(numbers)