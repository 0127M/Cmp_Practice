

#Rule 1
'''In case inharitance by child class we can access all variable from the '''


class P:

    a = 10
    def __init__(self):
        self.b = 20

    def m1(self):
        print("This is M1 method")

    @classmethod
    def m2(cls):
        print("This is class method")

    @staticmethod
    def m3():
        print("This is static method")


class C(P):
    pass


c = C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()