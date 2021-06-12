from abc import ABC,abstractmethod

class student(ABC):
    def __init__(self):
        print("Default constructor")
    @abstractmethod
    def price(self,x):
        pass

class deepak(student):
    def price(self,x):
        print("Body given by the child class")

obj=deepak()
obj.price(123)


