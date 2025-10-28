class dog:
    species = "dog"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

husky = dog("Blu", 10)
golden_retriever = dog("Woo", 15)

print("Blu is a {}".format(husky.__class__.species))
print("Woo is a {}".format(golden_retriever.__class__.species))
print("{} is {} years old".format(husky.name, husky.age))
print("{} is {} years old".format(golden_retriever.name, golden_retriever.age))