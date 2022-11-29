while(True):
    print("Print q to exit : ")
    a = input("Enter your number - ")
    if a == 'q':
        break;
    try:
        a = int(a)
        if a > 10:
            print(str(a) + " is greater than 10\n")
        else:
            print(str(a) + " is less than 10\n")
    except Exception as e:
        print(f"You've entered an wrong value : {e}")

print("Thank you for playing!\n\n")
