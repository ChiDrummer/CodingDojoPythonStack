class Car():
    def __init__(self, price, speed, fuel, milage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milage = milage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def displayInfo(self):
        print "Price: {}".format(self.price)
        print "Speed: {}".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Milage: {}".format(self.milage)
        print "Tax: {}".format(self.tax)


Car1 = Car(5000, 50, "Full", 3456)
Car2 = Car(50000, 100, "Empty", 7890)
Car3 = Car(55000, 40, "Half_Full", 24567)
Car4 = Car(45000, 30, "Full", 12345)
Car5 = Car(8000, 20, "Empty", 56779)
Car6 = Car(9000, 10, "Half-Empty", 76543)

Car1.displayInfo()
Car2.displayInfo()
Car3.displayInfo()
Car4.displayInfo()
Car5.displayInfo()
Car6.displayInfo()

        


