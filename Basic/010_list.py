# define with []

data = ["Rakib", 16, 10000.00, 1, 2, 3, 4, 5]
print(data)
print(data[0])  # first item
print(data[-1])  # last item
print(data[0:3])  # list from index 0 to 2 (3 will not include)

print("\n")
print("FOR LOOP:")
for i in data:
    print(i)

print("\n")
print("ADD or INSERT")
data.append(6)
print(data)
data.insert(1, "Hasan")
print(data)

print("\n")
print("LIST LENGTH")
print(len(data))


print("\n")
print("WHILE LOOP:")
i = 0
while i < len(data):
    print(data[i])
    i = i+1


print("\n")
print("CLEAR LIST:")
data.clear()
print(data)
