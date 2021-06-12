class SelfKeyword:
    def method1(self,first):
        self.first=first
obj= SelfKeyword()
obj.method1(123)
print("Value of first variable is", obj.first)
