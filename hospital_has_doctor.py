class Doctor:
    hospt_name="appolo"
    def __init__(self,doctor_name,specialization):
        self.doctor_name=doctor_name
        self.specialization=specialization
    def hospt(self):
        print("hospital is located in nrt")
class Hospital:
    def __init__(self,doctor_name,specialization,location):

        self.doctor=Doctor(doctor_name,specialization)
        self.location=location
    def doctor_details(self):
        print("hospital name is:",self.doctor.hospt_name)
        print("doctor name is:",self.doctor.doctor_name)
        print("doctor specialization  is: ",self.doctor.specialization)
        print("hospital is located in:",self.location)
        self.doctor.hospt()
hospital_obj=Hospital("ram","heart","nrt")
hospital_obj.doctor_details()
