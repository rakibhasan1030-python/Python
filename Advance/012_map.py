data = [1,2,3]

def squre(a):
    return a * a;

print("Method 1 : (without map)")
temp = []
for i in data:
    temp.append(squre(i))
print(temp)

print('\n')

print("Method 1 : (with map)")
print(list(map(squre, data)))