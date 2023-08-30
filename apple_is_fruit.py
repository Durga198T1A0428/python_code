class fruit:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def fruit_taste(self):
        print("fruit is so tasty")
class apple(fruit):
    def __init__(self,name,price,colour):
        super().__init__(name,price)
        self.colour=colour
    def apple_taste(self):
        print("The fruit's name is {name},fruit's cost is {price} and fruit's colur is {colour}".\
              format(name=self.name,price=self.price,colour=self.colour))
apple_obj=apple("apple",20,"red")
apple_obj.apple_taste()
apple_obj.fruit_taste()

