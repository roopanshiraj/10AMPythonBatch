class car:
    def __init__(self,name,price):
        self._name=name
        self.price=price
    def description(self):
        print("name is", self._name+ "\n" "price is ",self.price)