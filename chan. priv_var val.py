class computer:
    def __init__(self):
        self.__max_price=900
    def sell(self):
        print("Selling price:",self.__max_price)
    def setMaxprice(self,price):
        self.__max_price=price
c=computer()
c.sell()
c.__max_price=1000
c.sell()
c.setMaxprice(1000)
c.sell()