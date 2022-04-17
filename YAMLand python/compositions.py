'''compositons means if you will going to use
class member in any other class '''

#
# class Engine:
#     a = 10
#     def __init__(self):
#         self.name = 20
#
#     def display(self):
#         print("this is name of the Engine :-" ,self.name)
#
#
# class Car:
#
#     def __init__(self):
#         self.engine = Engine()
#
#     def display1(self):
#         print(self.engine.a)
#         print(self.engine.name)
#
# c = Car()
# c.display1()
#
#
# '''You need to write the car'''
#
# class Car:
#     '''This will provide car
#     details of employee'''
#     def __init__(self, cname , model_No, color):
#         self.cname = cname
#         self.model_No = model_No
#         self.color = color
#
#     def car_details(self):
#         print(f"name of car :-  {self.cname} , model number :- {self.model_No} , color :- {self.color}")
#
# class Employee:
#
#     def __init__(self, ename ,eno, Car):
#         self.ename = ename
#         self.eno = eno
#         self.car = Car
#
#     def eandc_details(self):
#         print(f' employee name :- {self.ename}')
#         print(f' employee name :- {self.eno}')
#         self.car.car_details()
#
#
# c = Car('maruti', 'maruti 123', 'red')
# e = Employee('nitin',15646, c)
# e.eandc_details()




