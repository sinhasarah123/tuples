from abc import ABC, abstractmethod

class AbsClass(ABC):

    
    def print(self, x):
        print(f"passed value is: {x}")
    def task(self):

        print("This is an abstract method")
    def task_1(self):
        print("we are in a task method")
        pass
class testClass(AbsClass):
           
                pass

test_obj= testClass()
test_obj.task_1()
test_obj.print(10)