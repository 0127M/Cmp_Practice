from Abstraction_One import Layer_One

class Layer_second(Layer_One):
    # def __init__(self):
    #     super().__init__(self)

    def First_Name_Last_Name(self):
        print(self.First_Name + self.Last_Name , self.number)


    def First_Name_Second_Name(self):
        print(self.First_Name + self.Second_Name)


a = Layer_second('A','B','C',123)
a.First_Name_Last_Name()
a.First_Name_Second_Name()


#
# class Employee:
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender
#
# class Salary:
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender
#     def jump(self):
#         print(self.name,self.salary)
#
# class Male(Salary,Employee):
#     def __init__(self,name,gender,occupation):
#         self.occupation=occupation
#         super().__init__(name,gender)