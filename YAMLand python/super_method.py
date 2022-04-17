

#
# class P:
#     '''This is perent class '''
#     a = 110
#     def __init__(self):
#         self.b = 102
#
#
# class C(P):
#     c = 1030
#     def __init__(self):
#         super().__init__()
#         self.d = 140
#
# c = C()
# print(c.a,c.b,c.c,c.d)
#
# #Rule
# '''If we need to extend functionality then we need to go for inharitance'''
# '''If we need to use only the variable or member of the class then we need use composition'''
#
#
#
# class P:
#     '''This is perent class '''
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class E(P):
#     def __init__(self,salary,department,name, age):
#         super().__init__(name, age)
#         self.salary = salary
#         self.department = department
#
#     def display(self):
#         print("This is details of the employee")
#         print(self.name , self.age ,self.salary , self.department )
#
#
# e = E(1565,'mechnical','nitin',26)
# e.display()

#Rule
'''Super method with method '''

# class P:
#     '''This is perent class '''
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

    # def display(self):
    #     print("This is details of Employee")
    #     print(self.name)
    #     print(self.age)


# class C(P):
#
#     def __init__(self, name, age, roll, mark ):
#         super().__init__(name, age)
#         self.roll = roll
#         self.mark = mark
#
#
#     def diaplay1(self):
#         super().display()
#         print(self.roll)
#         print(self.mark)
#
#
# c = C("nitin",26,6646,666)
# c.diaplay1()


#Rule
'''In child class static method we can use super method'''
#RuntimeError: super(): no arguments
'''This will be return no arg in super means we can't use 
any super inside the child method '''
#
# class P:
#
#     '''In this class we are define all method
#     for use '''
#
#     def __init__(self):
#         print("p constructor")
#
#     def m1(self):
#         print('P instance method')
#
#     @classmethod
#     def m2(cls):
#         print("p class method ")
#
#     @staticmethod
#     def m3():
#         print("p static method")
#
# class C(P):
#     @staticmethod
#     def m4():
#         super().m1()
#         super().m2()
#         super().m3()
#
# C.m4()

#HOW WE CAN USE PARENTS CLASS STATIC METHOD IN CHILD CLASS STATIC METHOD

class P:

    @staticmethod
    def m1():
        print("Parent class static methods ")

class C(P):

    @staticmethod
    def m1():
        print("This is child class static methods")
        super(C,C).m1()
C.m1()