name = "Datacamp"
type_of_company = "Educational"

## enclose your variable within the {} to display it's value in the output
print(f"{name} is an {type_of_company} company.")

#--------------------------------------


def greet(name):
    return "Hello, " + name
name = "Datacamp"
print(f"{greet(name)}")


#-----------------------------------------

string = "datacamp is an educational company."
print(f"{string.title()}")

#------------------------------------------

class Sample:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    ## this method will be called when we print the object
    def __str__(self):
        return f'{self.name} is {self.age} years old.'

john = Sample("John", 19)

## it'll wake up the __str__() method
print(f"{john}")


#-----------dictionaries----------------------



