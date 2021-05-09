class sameClassCreation:
    a=2
    def method1(self):
        print("Printing in same class")
ob= sameClassCreation()
ob.method1()
print("value of a is", ob.a)
