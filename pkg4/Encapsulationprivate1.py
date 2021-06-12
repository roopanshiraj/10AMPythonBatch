class car:
    def __init__(self,name,price):
        self.__name=name
        self.price=price
    def __description(self):
        print("name is", self.__name+ "\n" "price is ",self.price)