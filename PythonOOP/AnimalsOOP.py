class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        

    def walk(self):
        self.health = self.health - 1
        return self

    def run(self):
        self.health = self.health - 5
        return self

    def displayHealth(self):
        print "Your {} has {} health left".format(self.name, self.health)
        return self

class Dog(Animal):
    def __init__(self, name):
        health = 100
        super(Dog, self).__init__(name, health)
        
    def getPet(self):
        self.health = self.health + 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        health = 170
        super(Dragon, self).__init__(name, health)
        
    def fly(self):
        self.health = self.health - 10
        return self
    
    def displayHealth(self):
        print "I AM DRAGON!!! Health is: {}".format(self.health)
        return self

"""Create an instance of the Animal, have it walk() three times, run() twice, and finally displayHealth() to confirm that the health attribute has changed"""

bear = Animal("Bear", 100)
bear.walk().walk().walk().run().run().run().displayHealth()

"""Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth()."""

Dog("Damn Doggie").walk().walk().walk().run().run().displayHealth()


Dragon("Falcor").fly().displayHealth()





        




