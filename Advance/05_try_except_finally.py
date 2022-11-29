try:
    a = int(input("Inter a number : "))
    b = a * 30
except Exception as e:
    print(f"Error occured : {e}")
    exit()
finally:
    # finally will execute at any cost though the program exit in exeption, it'll execute
    # it used for clean-up. suppose program use some service and then you've to close the service before exit the program
    # here finally works well
    print("We're done!")
