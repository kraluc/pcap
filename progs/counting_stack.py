# Counting stack

# Your task is to extend the Stack class behavior in such a way
# so that the class is able to count all the elements that are pushed
# and popped (we assume that counting pops is enough).
# Use the Stack class we've provided in the editor.


class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        return self.__stk.pop()


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__pop_count = 0
        self.__push_count = 0
        self.__counter = 0

    def push(self, val):
        Stack.push(self, val)
        self.__push_count += 1
        self.__counter += 1

    def pop(self):
        self.__pop_count += 1
        self.__counter += 1
        return Stack.pop(self)

    def get_counter(self):
        return self.__pop_count


stk = CountingStack()

for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
