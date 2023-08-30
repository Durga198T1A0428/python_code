class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def person_details(self):
        print(self.name,"wants to become a doctor")
class Doctor(Person):
    def __init__(self,name,age,gender,doctor_specialization,doctor_location):
        super().__init__(name,age,gender)
        self.doctor_specialization=doctor_specialization
        self.doctor_location=doctor_location
    def doctor1(self):
        print(self.doctor_specialization)
        print(self.doctor_location)

doctor_obj=Doctor("asif",22,"male","heart","nrt")
doctor_obj.doctor1()
doctor_obj.person_details()