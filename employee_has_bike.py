class Bike:
    a="300"
    def __init__(self,name,cost,speed):
        print("bike details")
        self.name=name
        self.cost=cost
        self.speed=speed
    def bike1(self):
        print(" favouraite bike")
class Employee:
    def __init__(self,name,cost,speed,salary):
        self.bike=Bike(name,cost,speed)
        self.salary=salary
    def go_for_a_ride(self):
        print("bike model is:",self.bike.a)
        print("bike name is:",self.bike.name)
        print("bike cost is",self.bike.cost)
        print("bike speed is:",self.bike.speed)
        print("employee salary is:",self.salary)
        self.bike.bike1()
bike_obj=Employee("bullet","2.5l","90",30000)
bike_obj.go_for_a_ride()