class Parent1:
    def __init__(self,parent1_name):
        self.parent1_name=parent1_name
    def parent1_method(self):
        print("inside parent 1")
        print("Parent1 name is:", self.parent1_name)
class Parent2:
    def __init__(self,parent2_name):
        self.parent2_name = parent2_name
    def parent2_method(self):
        print("inside parent 2 method")

class Child(Parent1,Parent2):
    def __init__(self,parent1_name,child_name):
        super().__init__(parent1_name)
        self.child_name=child_name
    def child_method(self):
        print("inside child ")
        print("child name is:",self.child_name)
class Subchildren(Child):
    def __init__(self,parent1_name,child_name,subchild_name):
        super().__init__(parent1_name,child_name)
        self.subchild_name = subchild_name
    def subchildren_method(self):
        print("inside subchildren")
        print("subchildren name is:", self.subchild_name)
class Child1(Subchildren):
    def __init__(self, parent1_name,child_name,subchild_name,child1_name):
        super().__init__(parent1_name,child_name,subchild_name)
        self.child1_name =child1_name


    def child1_method(self):
        print("inside child1")
        print("child1 name is:",self.child1_name)
class Child2(Subchildren):
    def __init__(self, parent1_name, child_name, subchild_name, child2_name):
        super().__init__(parent1_name, child_name, subchild_name)
        self.child2_name = child2_name
    def child2_method(self):
        print("inside the child 2 method")
        print("child2 name is:", self.child2_name)
child1_obj=Child1("suri","satish","dinesh","bhagavan")
child1_obj.parent1_method()
child1_obj.parent2_method()
child1_obj.child_method()
child1_obj.subchildren_method()
child1_obj.child1_method()
child2_obj=Child2("ram","raju","rajesh","revanth")
child2_obj.child2_method()