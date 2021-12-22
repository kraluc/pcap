class Left:
    var = "L"
    var_left = "LL"

    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"

    def fun(self):
        return "Right"


class Sub1(Left, Right):
    pass


class Sub2(Right, Left):
    pass


obj1 = Sub1()
obj2 = Sub2()

print(obj1.var, obj1.var_left, obj1.var_right, obj1.fun())
print(obj2.var, obj2.var_left, obj2.var_right, obj2.fun())
