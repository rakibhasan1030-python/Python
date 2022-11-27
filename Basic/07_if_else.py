user_age = input("Write your age - ")
age = int(user_age)

#age = 15

if age > 0 and age < 10:
    print("Child")
elif age > 10 and age < 18:
    print("Teenage")
elif age > 18 and age < 30:
    print("Adult")
elif age > 30 and age < 50:
    print("Middle age")
else:
    print("Old")
