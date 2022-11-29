while(True):
    print("Print q to exit : ")
    a = input("Enter your number - ")
    if a == 'q':
        break;
    try:
        a = int(a)
        c = 100/a
        print(f"Your number is : {c}\n")
    except ValueError as v:
        print(f"Please, enter a valid value : {v}\n")
    except ZeroDivisionError as z:
        print(f"Please, enter a valid value : {z}\n")

print("Thank you for playing!\n\n")