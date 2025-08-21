
class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if self.a < other.a:
            return "a is less than other object"
        else:
            return "a is greater than or equal to other object"

    def __eq__(self, other):
        if self.a == other.a:
            return "a is equal to other object"
        else:
            return "a is not equal to other object"

ob1 = A(5)
ob2 = A(10)
print("passed values", ob1.a, ob2.a)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print("passed values", ob3.a, ob4.a)
print(ob3 == ob4)