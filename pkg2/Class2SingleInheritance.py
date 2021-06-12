from pkg2.Class1SingleInheritance import Class1SingleInheritance

class Class2SingleInheritance(Class1SingleInheritance):
    def method2(self):
        print("I am the child class method")
ob= Class2SingleInheritance()
ob.method1()
ob.method2()
                                                           #Single Level Inheritance