class dog:
    def __init__(self,name,bark,eat,drink,sleep):
        self.name=name
        self.bark=bark
        self.eat=eat
        self.drink=drink
        self.sleep=sleep
    def add_dog_details(self):
        print("dog details")
        print("Dog's name is {}.".format(self.name),"It barks with a {}.".format(self.bark),"It always likes to eat {}".format(self.eat),"and drink {}.".format(self.drink),"Daily, it sleep around {}".format(self.sleep))
        # print("it barks {}".format(self.bark))
        # print("it always like to eat {}".format(self.eat))
        # print("and drink {}".format(self.drink))
        # print("daily it sleep around {}".format(self.sleep))
dog_details1=dog('jimmy','high pitch and repeated','chicken','milk',9.45)
dog_details1.add_dog_details()
dog_details2=dog('snoopy','low pitch','bread','water',7.45)
dog_details2.add_dog_details()