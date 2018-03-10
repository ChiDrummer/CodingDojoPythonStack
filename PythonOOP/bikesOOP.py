class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.total_miles = 0

    def displayInfo(self):
        print "Price is: {}, Max Speed is: {}, Total Miles are: {}".format(self.price, self.max_speed, self.total_miles)
    
    def ride(self):
        print "Riding FORWARD!!"
        self.total_miles += 10
    
    def reverse(self):
        print "Riding BACKWARD!!"
        self.total_miles -= 5

bike1 = Bike(500, 100)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()








