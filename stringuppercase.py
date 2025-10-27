class is_string():
    def __init__(self):
      self.str1=""
    def getstring(self):
            self.str1=input("enter a string:")
        

    def printstring(self):
        print("this string is:",self.str1.upper())
str1=is_string()
str1.getstring()
str1.printstring()