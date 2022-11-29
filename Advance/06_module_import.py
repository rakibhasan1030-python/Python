import sum_module
# this will not print expected value if we don't put main condition in module file. this file will will run whole module.
sum = sum_module.sum(12)
print(f"Total - {sum}")
