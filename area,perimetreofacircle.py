class circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return circle.pi*self.radius*self.radius
    def perimeter(self):
        return 2*circle.pi*self.radius