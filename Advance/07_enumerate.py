list = ["Rakib", 16, 10000.00, False]

print("General approach:")
# if we want to print item with index in python, in basic we do -
index = 0
for item in list:
    print(f"Index : {index} - {item}")
    index += 1


print("\n\nEnumerate approach:")
# but we can do it easily with enumerate key words, it will add an counter to the list and retuns it!
# as we did to the above program manually
for index, item in enumerate(list):
    print(f"Index : {index} - {item}")
