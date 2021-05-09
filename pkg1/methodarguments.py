class ClassA:
    a = 12

    def method1(self):
        print("I am the first method of the class")

    def method2(self, *name):
        print("value of firstname is ", name[0])
        print("value of lastname is ", name[2])

    def method3(self,firstname,lastname):
        print("value of firstname is ",firstname)
        print("value of lastname is ",lastname)

    def method4(self, **fname):
        print("value of firstname is", fname["firstname"])
        print("value of middlename is", fname["middlename"])
        print("value of lastname is", fname["lastname"])

    def method5(self,fname="Roops"):
        print("value of firstname",fname)

obj = ClassA()
obj.method3(firstname="shiva",lastname="chaudhary")
obj.method3(lastname="chaudhary",firstname="shiva")
obj.method3("chaudhary","shiva")
obj.method2("manilla","himanshu","prateek","gayathri")
obj.method4(firstname="Deepak", middlename="Roy", lastname="Chanana")
obj.method5()
obj.method5("Sahil")