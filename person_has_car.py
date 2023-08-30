class Car:
    a="A4"
    def __init__(self,name,cost,speed):
        print("car details")
        self.name=name
        self.cost=cost
        self.speed=speed
    def car1(self):
        print(" audi car has high futures")
class person:
    def __init__(self,name,cost,speed):
        self.car=Car(name,cost,speed)
    def go_for_a_ride(self):
        print("car model is:",self.car.a)
        print("car name is:",self.car.name)
        print("car cost is",self.car.cost)
        print("car speed is:",self.car.speed)
        self.car.car1()
car_obj=person("audi","40l","70")
car_obj.go_for_a_ride()