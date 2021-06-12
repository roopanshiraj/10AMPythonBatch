class MethodOverloading2:
    def method1(self):
        print("I am the default method of the class")
    def method1(self,a):
        print("I am the one parameterized method of the class")
ob= MethodOverloading2()
ob.method1(20)