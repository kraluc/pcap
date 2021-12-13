# Stack


#    we want the class to have one property as the stack's storage - we have to "install" a list inside each object of the class (note: each object has to have its own list - the list mustn't be shared among different stacks)
#    then, we want the list to be hidden from the class users' sight.


class Stack:
    def __init__(self):  # Defining the constructor function
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        self.__sum -= Stack.pop(self)

    def get_sum(self):
        return self.__sum


stack1 = AddingStack()
print("n sum\n--------")

for n in range(10):
    stack1.push(2 * n)
    print(n, " ", stack1.get_sum())

print()

for n in range(8, -1, -1):
    stack1.pop()
    print(n, " ", stack1.get_sum())

# # Example 1
# stack_object = Stack()  # Instantiate the object
# for n in range(1, 4):
#     stack_object.push(n)

# for n in range(3):
#     print(stack_object.pop())

# print()

# # EXample 2
# stack_object1 = Stack()
# stack_object2 = Stack()

# stack_object1.push(3)
# stack_object2.push(stack_object1.pop())

# print(stack_object2.pop())

# print()

# # Example 3
# little_stack = Stack()
# another_stack = Stack()
# funny_stack = Stack()

# little_stack.push(1)
# another_stack.push(little_stack.pop() + 1)
# funny_stack.push(another_stack.pop() - 2)

# print(funny_stack.pop())
