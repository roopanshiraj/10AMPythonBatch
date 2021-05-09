class File1:
    a=12
    def method1(self):
        print("I am the first method of the class")

    def method2(self,fname):
        print("value of firstname is ",fname)

obj= File1()
obj.method1()
obj.method2("tom")