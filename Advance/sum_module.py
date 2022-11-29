def sum(a):
    try:
        return int(a) + 5
    except Exception as e:
        print(f"Error : {e}")


# if we don't put this confdition, every place where this module will use, execute these lines of codes under the condition.
# which we don't want, this code will run only from this file.
# __name__ is the name of this file which is "sum_module"
if __name__ == "__main__":
    a = input("Enter a number - ")
    print(f"Your answer is : {sum(a)}")
