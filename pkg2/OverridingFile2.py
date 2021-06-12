from pkg2.OverridingFile1 import OverridingFile1

class OverridingFile2(OverridingFile1):
    def method1(self):
        print("Overriden by child class")
ob= OverridingFile2()
ob.method1()

