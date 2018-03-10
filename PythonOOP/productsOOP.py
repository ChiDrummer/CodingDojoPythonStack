class Product():
    def __init__(self, itemName, price, weight, brand):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.status = "FOR SALE"

    def sell(self):
        self.status = "SOLD"
        return self

    def addTax(self, taxes):
        self.price = self.price * taxes + self.price
        return self

    def returnItem(self, condition):
        if condition == "defective":
            self.price = 0
        elif condition == "like new":
            self.status = "for sale, again...."
        elif condition == "opened":
            self.status = "used"
            self.price = self.price - (self.price * .20)
        return self
    
    def displayInfo(self):
        print "Your Product Information:"
        print "Item Name: {}".format(self.itemName)
        print "Price: ${}".format(self.price)
        print "Weight: {}".format(self.weight)
        print "Brand: {}".format(self.brand)
        print "Status: {}".format(self.status)
        return self

Item1 = Product("Cheeze Its", 3.95 , "20 ozs", "Nabisco")
Item2 = Product("Triscuts", 4.99, "1 lb", "Kraft")
Item3 = Product("Wheat Thins", 2.50, ".5 lbs", "Keebler")
Item4 = Product("Gold Fish", 3.75, "2 lbs", "Prepridge Farms")

Item1.addTax(.10).sell().displayInfo()
Item2.returnItem("defective").displayInfo()
Item3.returnItem("opened").displayInfo()
Item4.returnItem("like new").addTax(.10).displayInfo()





    


