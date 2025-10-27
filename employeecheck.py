class Employee:
    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("Employee deleted")
    def create_object():
        print("Creating Employee Object")
        obj = Employee()
        return obj
print("calling create_object method")
obj = Employee.create_object()
print("exiting the program")