class employee:
    company_name="tcs"
    def __init__(self,name,id,salary,age):
        self.name=name
        self.id=id
        self.salary=salary
        self.age=age
    def employee_hike(self,percentage):
        hike_amount=self.salary*(percentage/100)
        self.salary=self.salary+hike_amount
employee_1=employee("durga",428,10000,22)
employee.company_name
percentage_input = float(input("Enter the percentage hike: "))
employee_1.employee_hike(percentage_input)
print("after adding the hike {} then the Updated salary will be:{}".format(percentage_input, employee_1.salary))


