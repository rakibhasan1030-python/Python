try:
    a = int(input("Inter a number : "))
    b = a * 30
except Exception as e:
    print(f"Error occured : {e}")
else:
    print("try successfully completed!")
