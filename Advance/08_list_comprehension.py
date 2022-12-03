# syntax = [expression for item in iterable condition(if have)]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
evenData = []
oddData = []

print("General approach:")
for item in data:
    if item % 2 == 0:
        evenData.append(item)
    else:
        oddData.append(item)
print(f"Even numbers : {evenData}\nOdd numbers : {evenData}")

print("\n\nComprehensive approach:")  # one liner or shortcut
evenData = [i for i in data if i % 2 == 0]
evenData = [i for i in data if i % 2 != 0]
print(f"Even numbers : {evenData}\nOdd numbers : {evenData}")
