class MethodOverloading3:
    def method1(self,a):
        print("I am the one parameterized method of the class")
    def method1(self):
        print("I am the default method of the class")
ob= MethodOverloading3()
ob.method1()                                                             #always latest will be called