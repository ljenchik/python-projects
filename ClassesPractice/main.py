# name should be singular, capital letter first, camelcase
# __init__ automatically calls when a new instance of the class in instantiating
# self refers to each individual instance, first parameter for each method in the class
class User:
    # class variables or attributes, exists on class
    active_users = 0

    # class methods
    @classmethod
    def display_active_users(cls):
        return cls.active_users

    @classmethod
    # parses data from csv file: "John, Smith, john@gmail.com, 23"; or for validation
    def from_string(cls, data_str):
        first_name, last_name, email, age = data_str.split(',')
        return cls(first_name, last_name, email, age)

    # instance methods
    def __init__(self, first_name, last_name, email, age):
        # instance attributes
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        User.active_users += 1  # changes when a new user is created

    # create a user instance representation
    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}"

    def welcome(self):
        return f"Hello {self.first_name} {self.last_name}"

    def initials(self):
        return f"{self.first_name[0].upper()}{self.last_name[0].upper()}"

    def likes(self, thing):
        return f"{self.first_name} likes {thing}"

    def is_senior(self):
        if self.age >= 65:
            return True
        else:
            return False

    def logout(self):
        User.active_users -= 1
        return f"{self.first_name} is logged out"


user1 = User("sam", 'baker', "sam@gmail.com", 75)
print(user1.first_name)
print(user1.welcome())
print(user1.initials())
print(user1.likes('history'))
print(user1.is_senior())
user2 = User("misha", 'baker', "sam@gmail.com", 25)
print(User.active_users)
user2.logout()
print(User.active_users)
print(User.display_active_users())
print(user2.display_active_users())
user3 = User("sam", 'baker', "sam@gmail.com", 75)
user4 = User("sam", 'baker', "sam@gmail.com", 75)
print(User.display_active_users())
user5 = User.from_string("Olena,Pelagenko,olena@gmail.com, 42")
print(user5.first_name)
print(user5.email)
print(user5.age)
print(user5)
