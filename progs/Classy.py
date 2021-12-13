class Classy:
    def method(self, par):
        print("method", par)


obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)

# EXample# 2:  The self parameter is used
# to obtain access to the object's instance and class variables.
class Classy:
    varia = 2

    def method(self):
        print(self.varia, self.var)


obj = Classy()
obj.var = 3
obj.method()

# Example# 3:
class Classy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()


obj = Classy()
obj.method()


# Example 4:
class Classy:
    def __init__(self, value):
        # cannot return a value + cannot be invoked directly
        self.var = value


obj_1 = Classy("object")

print(obj_1.var)


# Example 5: constructor with default variable value
class Classy:
    def __init__(self, value=None):
        self.var = value


obj_1 = Classy("object")
obj_2 = Classy()

print(obj_1.var)
print(obj_2.var)


# Example 6: private methods
class Classy:
    def visible(self):
        print("visible")

    def __hidden(self):
        print("hidden")


obj = Classy()
obj.visible()

try:
    obj.__hidden()
except AttributeError as err:
    print("failed:", err)

obj._Classy__hidden()


# Example 7
class Classy:
    varia = 1

    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)
