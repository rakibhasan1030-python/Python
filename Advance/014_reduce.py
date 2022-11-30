from functools import reduce


def sum(a, b): return a+b


data = [1, 2, 3, 4, 5]
# reduce add values in a list sequestially
# here, 1+3 = 3, 3+3 = 6, 6+4 = 10, 10+5 = 15
print(reduce(sum, data))  # output = 15
