class ExampleClass:
    varia = 1

    def __init__(self, val=1):
        ExampleClass.varia = val
        self.variable = val


print(ExampleClass.__dict__)

example_object = ExampleClass(2)

print()
print("class __dict__:\n>> %s" % ExampleClass.__dict__)
print()
print("instance __dict__:\n>> %s" % example_object.__dict__)


print(hasattr(ExampleClass, "varia"))
print(hasattr(ExampleClass, "prop"))
print(hasattr(example_object, "variable"))
print(hasattr(example_object, "varia"))

print(ExampleClass.__bases__)
