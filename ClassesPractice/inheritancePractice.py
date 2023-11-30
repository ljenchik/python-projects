class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self):
        return f"this animal says hello"

# Cat inherits Animal
class Cat(Animal):
    def __init__(self, name, breed, toy, sound):
        # refers to a parent class
        super().__init__(name, species="Cat")
        # Animal.__init__(self, name, species)
        self.breed = breed
        self.toy = toy
        self.sound = sound

    def play(self):
        print(f"{self.name} plays with {self.toy}")

    def make_sound(self):
        return f"this animal says {self.sound}"


class Dog(Animal):
    def __init__(self, name, breed, food):
         # refers to a parent class
        super().__init__(name, species="Dog")
        self.breed = breed
        self.food = food

    def make_sound(self):
        return f"this animal says bark"


blue = Cat("Blue", "Russian", "String", "meow")
timmy = Dog("Timmy", "Cocker", "meat")
animal = Animal('Daisy', "cow")

print(blue)
print(timmy)
print(animal)

print(blue.make_sound())
print(timmy.make_sound())
print(animal.make_sound())
