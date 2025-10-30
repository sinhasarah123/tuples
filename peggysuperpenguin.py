class bird:
    def __init__(self):
        print("Bird is ready")
    def whoisThis(self):
        print("Bird")
class penguin(bird):
    def __init__(self):
                super().__init__()
                print("Penguin is ready")
    def whoisThis(self):
                print("Penguin is a bird")
    def swim(self):
                print("Penguin can swim")
    def run(self):
                print("Penguin can run")
peggy = penguin()
peggy.whoisThis()
peggy.run()
