class vehicle:
    def __init__(self, vehicle_number):
        self.vehicle_number = vehicle_number

    def vehicle_speed(self):
        pass
class car(vehicle):
    def __init__(self,vehicle_number,car_name,price,model):
        super().__init__(vehicle_number)
        self.car_name = car_name
        self.price = price
        self.model = model

    def car_speed(self):
        print("The car name is {car_name},it's model is {model},car cost is {price} and car number is {vehicle_number}".\
              format(car_name=self.car_name,model=self.model,price=self.price, vehicle_number= self.vehicle_number))
car_obj=car("AP 07 8339","benz",8000000,"benz-c")
car_obj.car_speed()
car_obj.vehicle_speed()


