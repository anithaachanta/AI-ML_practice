class Student:
    def __init__(self,name,age,skills):
        self.name=name
        self.age=age
        self.skills=skills
    def display(self):
        print(self.name,self.skills)
student1=Student("anitha",22,"python")
student1.display()