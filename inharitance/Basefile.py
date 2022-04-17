#means if you want to  add the details about the class you need to write
#in doc string

# class Student:
#     '''this student class for required data'''
# print(Student.__doc__)
# help(Student)


#-----------------------------------------------------
#Basic class

# class Student:
#     def __init__(self,name, roll):
#         self.name = name
#         self.roll = roll
#
#     def talk(self):
#         print(f'Student name is {self.name} and roll number is {self.roll}')
#
# # here we need to provide all details in the class name
# s1 = Student('nitin',49)
# s1.talk()


#-------------------------------------------------------
#
# class Student:
#     def __init__(self):
#         print('This is constructor')
#     def m1(self):
#         print('This is method one ')
# s1 = Student() #if u execute only this class object the constructor will execute

# s1.m1()
# s1.m1()
#--------------------instance variable ------------------------------------
#
# class Student:
#     def __init__(self):
#         self.name='nitin'
#
# e=Student()
# print(e.__dict__) #this will provide the object of the name

#-------------------------------------------------------------------------


# class Student:
#
#     def __init__(self):
#         self.a = 10
#     def m1(self):
#         self.b = 20
#
# s1 = Student()
# s1.m1() #you need to call this method to if you want to add instance method
# s1.c = 30
# print(s1.__dict__)

#Instance variavle can access inside the class by self
#out side of the class by class object reference

#Delete
#Delete varibale also going through the same method
#del self.variablename
#del objectrefreance.varible name
#--------------------------------------------------------------------------


# class Student:
#     """This is class of the of the variable"""
#     def __init__(self,name,mark):
#         self.name = name
#         self.mark = mark
#     def grade(self):
#         print(f'Student name is {self.name} and marks is {self.mark}')
#     def display_category(self):
#         if self.mark > 60:
#             print('Good marks ')
#         elif self.mark < 60:
#             print('Average marks ')
#         else:
#             print('Fail')
# Number = int(input('Enter number of student'))
# for i in range(Number):
#     name  = input('Enter the name')
#     mark  = int(input("Enter the mark"))
#     s = Student(name,mark)
#     s.grade()
#     s.display_category()


#----------------------------------



A = 10
B = 20
C = 30
class Student:
    '''the student class you can say
    the process of setter and getter'''
    def setter(self,name):
        self.name = name

    def getter(self):
        return self.name

    def setter1(self, mark):
        self.mark = mark

    def getter1(self):
        return self.mark

Number = int(input("Enter student the number"))
for i in range(Number):
    s = Student()
    name  = input('Enter the name')
    s.setter(name)
    mark = int(input("Enter the number"))
    s.setter1(mark)

    print('Hi',s.getter())
    print('Your number is :',s.getter1())
    print()

print("name is nitin ")
print("name is nitin ")
print("name is nitin ")
print("name is nitin ")
print("name is nitin ")



#--------------------------------------------







