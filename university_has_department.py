class Department:
    name="jntuk"
    def __init__(self,branch,code):
        print("department details")
        self.branch=branch
        self.code=code
    def dept(self):
        print("ece")
class university:
    def __init__(self,branch,code):
        self.department=Department(branch,code)
    def university_details(self):
        print("university name is:",self.department.name)
        print("branch name is:",self.department.branch)
        print("branch code is:",self.department.code)
university_obj=university("ECE",4)
university_obj.university_details()

