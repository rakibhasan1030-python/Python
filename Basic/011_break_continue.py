# Break
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("BREAK")
for i in data:
    if i == 11:
        break
    print(i)

print("\n")

print("CONTINUE")
for i in data:
    if i == 11:
        continue
    print(i)
