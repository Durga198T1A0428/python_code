class Iphone:
    def __init__(self,cost,logo):
        self.cost=cost
        self.logo=logo
    def model1(self):
        print("iphone has more features")
class person:
    def __init__(self,cost,logo):
        self.person=Iphone(cost,logo)
    def iphone_use(self):
        print("iphone  cost is:",self.person.cost)
        print("iphone  logo is:", self.person.logo)
        self.person.model1()
person_obj=person(900000,"apple")
person_obj.iphone_use()