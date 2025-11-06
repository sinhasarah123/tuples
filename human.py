from abc import ABC, abstractmethod
class animal(ABC):

    def move(self):
        pass
class human(animal):

        def move(self):
            print("I can walk and run")
class snake(animal):

        def move(self):
            print("I slither on the ground")
class dog(animal):

        def move(self):
            print("I can walk and bark")
class lion(animal):

        def move(self):
            print("I can run and roar")
        R=human()
        R.move()
S= snake()
S.move()
D= dog()
D.move()
L= lion()
L.move()