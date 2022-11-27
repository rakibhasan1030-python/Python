name = "Rakib Hasan"

# uppercase,lowercase
print("UPPER-LOWER")
print(name.upper())
print(name.lower())
print("\n")

# find char
print("FIND CHAR")
print(name.find('H'))  # return index of the letter otherwise always return -1
print('R' in name)  # return true if exist, otherwise false
print("\n")

# replace char/sub-string/ string
print("REPLACE")
print(name.replace("H", 'R'))
print(name.replace("Hasan", 'H'))
print(name.replace("Rakib Hasan", 'R H'))
print("\n")
