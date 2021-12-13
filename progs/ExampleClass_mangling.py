class ExampleClass:
    __counter = 0

    def __init__(self, val=1):
        self.__first = val
        ExampleClass.__counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(
    example_object_1.__dict__,
    example_object_1._ExampleClass__first,
    example_object_1._ExampleClass__counter,
)
print(
    example_object_2.__dict__,
    example_object_2._ExampleClass__first,
    example_object_2._ExampleClass__counter,
)
print(
    example_object_3.__dict__,
    example_object_3._ExampleClass__first,
    example_object_3._ExampleClass__counter,
)

print()

# To access the Class Variable, you still need to do it via an existing instance object!
print(example_object_1.__dict__, example_object_1._ExampleClass__counter)

# This redefines a LOCAL object property that is different from the class variable! Don't do that!!
example_object_1._ExampleClass__counter -= 1
print(example_object_1.__dict__, example_object_1._ExampleClass__counter)

print(example_object_2._ExampleClass__counter)
# This accesses the class variable
print(example_object_1._ExampleClass__counter)

example_object_4 = ExampleClass(8)
print(example_object_4.__dict__, example_object_4._ExampleClass__counter)
print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
