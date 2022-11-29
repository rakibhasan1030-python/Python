def addValue(a):
    try:
        return int(a) + 44
    except:
        raise ValueError("This function takes number only")


valid = addValue(6)
print(f"Your answer is : {valid}\n")


# invalid = addValue('a')
# print(f"Your answer is : {invalid('a')}")
