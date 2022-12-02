my_list = ["Rakib", 26, "Dhaka", 1207]
my_dic = {"apple": 1, "orange": 2, "pear": 3}
my_info = {"name": "ID", "id": 7928}


def one(name, id):
    print(name, id)


def two(**args):
    print(args)


def three(*args):
    print(args)


print("Unpack my_list :")
print(*my_list)

print("\n")

print("Unpack my_dic (print only keys) :")
print(*my_dic)

print("\n")

print("Pass my_info as param (* means it passes the keys as values):")
one(*my_info)

print("\n")

print("Pass my_info as param (** means it passes the values as values):")
one(**my_info)
