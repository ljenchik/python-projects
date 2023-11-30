class MyClass:
    def __init__(self, owner, age):
        self.owner = owner
        self.__age = age

    def get_owner(self):
        return self.owner

    def __get_age(self):
        return self.__age

    def set_owner(self, new_name):
        self.owner = new_name

    def set_age(self, new_age):
        self.__age = new_age

instance1 = MyClass("Olena", 34)
print(instance1.get_owner())
print(instance1._MyClass__age)
print(instance1._MyClass__get_age())

instance1.set_owner("Chris")
print(instance1.owner)
print(instance1.get_owner())


instance1.set_age(23)
print(instance1._MyClass__age)
print(instance1._MyClass__get_age())
