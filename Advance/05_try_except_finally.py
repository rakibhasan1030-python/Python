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
    # again if program exit in exept bloc, then only finally bloc will be execte, no code will execute after finally bloc
    print("We're done!")

print("This messege will not print if error occurs because except bloc program perform exit, otherwise it'll print easily!")
