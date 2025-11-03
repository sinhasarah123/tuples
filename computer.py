class computer:
    def __init__(self):
        self.maxprice = 900
    def sell(self):
            print("Selling Price: {}".format(self.maxprice))
            format(self.maxprice)
    def setMaxPrice(self, price):
        self.__maxprice = price 
c = computer()
c.sell()
c.setMaxPrice(1000)
c.sell()
c.maxprice = 1000
c.sell()
c.maxprice = 1000