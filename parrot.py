class parrot:
    species = "bird"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

Blue = parrot("Blu", 10)
Woo = parrot("Woo", 15)

print("Blu is a {}".format(Blue.__class__.species))
print("Woo is a {}".format(Woo.__class__.species))
print("{} is {} years old".format(Blue.name, Blue.age))
print("{} is {} years old".format(Woo.name, Woo.age))