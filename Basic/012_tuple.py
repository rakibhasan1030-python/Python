# define with ()

# cannot modify
data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11, 11, 11)
print(data.count(11))  # return total number of repeated items

# return first item index if the item is repeated otherwise return index
print(data.index(11))
