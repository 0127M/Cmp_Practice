from abc import ABC , abstractmethod
import yaml




class Layer_One(ABC):

    '''This is a Base class class of '''

    def __init__(self,First_Name, Last_Name, Second_Name, number):
        self.number = number
        self.First_Name = First_Name
        self.Second_Name = Last_Name
        self.Last_Name = Second_Name
        with open('Data.yaml') as f:
            base = yaml.load(f, Loader=yaml.FullLoader)
            # print(type(data))
            # for key, value in data.items():
            #     print(key)

            # print(base.get('cities'))
            print(base.get['cities'])

            # for key, value in a.items():
            #     print(key)

    @abstractmethod
    def First_Name_Second_Name(self):
        pass

    @abstractmethod
    def First_Name_Last_Name(self):
        pass
