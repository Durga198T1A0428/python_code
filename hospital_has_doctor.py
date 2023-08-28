class Doctor:
    hospt_name="appolo"
    def __init__(self,doctor_name,specialization):
        self.doctor_name=doctor_name
        self.specialization=specialization
    def hospt(self):
        print("hospital is located in nrt")
class hospital:
    def __init__(self,doctor_name,specialization):
        self.doctor=Doctor(doctor_name,specialization)
    def doctor_details(self):
        print("hospital name is:",self.doctor.hospt_name)
        print("doctor name is:",self.doctor.doctor_name)
        print("doctor specialization  is: ",self.doctor.specialization)
        self.doctor.hospt()
hospital_obj=hospital("ram","heart")
hospital_obj.doctor_details()
