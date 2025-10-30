class person(object):
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display (self):
            print("Name:",self.name)
            print("ID Number:",self.idnumber)
class employee(person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,idnumber)
    def display(self):
            person.display(self)
            print("ID Number:",self.idnumber)
            print("Salary:",self.salary)
            print("Post:",self.post)
emp=employee("Sarah Sinha",12345,50000,"Intern")
emp.display()