class File1:
    a=12
    def method1(self):
        print("I am the first method of the class")

    def method2(self,*name):
        print("value of firstname is ",name[0])
        print("value of middlename is ", name[1])
        print("value of lastname is ", name[2])

obj= File1()
obj.method1()
obj.method2("tom","dick","harry")