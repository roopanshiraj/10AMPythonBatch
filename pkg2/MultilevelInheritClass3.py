from pkg2.MultilevelInheritClass2 import MultilevelInheritClass2

class MultilevelInheritClass3(MultilevelInheritClass2):
    def method3(self):
        print("I am the child class method")
ob=MultilevelInheritClass3()
ob.method1()
ob.method2()
ob.method3()                                             #Multilevel Inheritance