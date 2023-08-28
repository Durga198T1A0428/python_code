class Bike:
    a="300"
    def __init__(self,name,cost,speed):
        print("bike details")
        self.name=name
        self.cost=cost
        self.speed=speed
    def bike1(self):
        print(" favouraite bike")
class employee:
    def __init__(self,name,cost,speed):
        self.bike=Bike(name,cost,speed)
    def go_for_a_ride(self):
        print("bike model is:",self.bike.a)
        print("bike name is:",self.bike.name)
        print("bike cost is",self.bike.cost)
        print("bike speed is:",self.bike.speed)
        self.bike.bike1()
bike_obj=employee("bullet","2.5l","90")
bike_obj.go_for_a_ride()