from pkg2.MultipleInheritFile1 import MultipleInheritFile1
from pkg2.MultipleInheritFile2 import MultipleInheritFile2

class MultipleInheritFile3(MultipleInheritFile1,MultipleInheritFile2):
    def method3(self):
        print("I am the child class method")


ob = MultipleInheritFile3()
ob.method1()
ob.method2()
ob.method3()
#print("value of deepak is", ob.deepak)                      #del is used for deleting the object and attribute(variable)
#del ob.deepak
#print("value of deepak is", ob.deepak)