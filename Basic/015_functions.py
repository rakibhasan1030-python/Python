# Functions : build-in, module, user-define


# Functions : build-in - int(), str(), float(), bool()

# Functions : module - import math
from math import sqrt
import math
# print(dir(math))  # math module functions
# print(sqrt(16))


# Functions : user define
def sum(a, b):
    print(a+b)


def sub(a, b=5):
    print(a-b)


print(sum(5, 10))
print(sub(15))
