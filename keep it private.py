class MyClass:
    __private_var = 27
    def __private_method(self):
        print("This is a private method")
    def hello(self):
        print("private_var:", self.__private_var)
obj = MyClass()
obj.hello()  
# obj.__private_method()  