class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "point({}, {})".format(self.x, self.y)
    p1= point (1,2)
    print (p1)