class MethodOverloading:
    def method1(self):
        print("I am the default method of the class")
    def method1(self):
        print("I am the one parameterized method of the class")
ob= MethodOverloading()
ob.method1()