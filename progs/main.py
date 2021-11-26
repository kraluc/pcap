from sys import path

# Modify the system path to include the module and packages location
path.append("../modules/")
path.append("../packages")
from module import suml, prodl


zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))
