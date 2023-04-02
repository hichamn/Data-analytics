# Python code to calculate mean and standard deviation of a list of numbers

import statistics

data = [1, 2, 3, 4, 5]

mean = statistics.mean(data)
stdev = statistics.stdev(data)

print("Mean of data is: ", mean)
print("Standard deviation of data is: ", stdev)
