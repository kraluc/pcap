# Example 1: __name__ returns the name of the class the object belongs to
# it is a CLASS private method, accessible from the Class (only).
class Classy:
    pass


print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)

# Can't access the private method __name__ from the object instance
try:
    print(obj.__name__)
except AttributeError as err:
    print("Failed", err)

# Example 2 -  __module__ contains the name of the File that contains the class
class Classy:
    pass


print(Classy.__module__)
obj = Classy()
print(obj.__module__)
