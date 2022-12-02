# split() = anyString.split(separator, maxSplit)

# split function separate words in a string according to white-space(by default) or user define character
# and return a list of these separated words
rakib = "Rakib Hasan"
splitedNames = rakib.split()
print(f"Splited with white space = {splitedNames}")
print("\n")


name = "This,is,a,string"
splitedNames = name.split(",")
print(f"Splited with (,) = {splitedNames}")
print("\n")


# split string with space count
# if i put parameter as 1,it'll divide until 1st white-space and ignore other white-space
# again,if i put parameter as 2,it'll divide until 2nd white-space and ignore other white-space

intro = "Hello this is Rakib Hasan"
splitedIntro = intro.split(" ", 1)
print(f"Splited and white-space limit is 1 = {splitedIntro}")
print("\n")


# input with split
name, age = input("Please, enter name and age : ").split()
print(f"Name = {name}\nAge = {age}")
