class ConstructorOverloading:
    def __init__(self):
        print("I am the Default constructor of the class")
    def __init__(self,a):
        print("I am one paramterized constructor of the class")
ob= ConstructorOverloading(5)
