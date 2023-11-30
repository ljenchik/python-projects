class BankAccount:
    def __init__(self, owner, pin, balance=0):
        self.owner = owner
        self.__balance = balance
        self.__pin = pin

    def __repr__(self):
        return f"It is {self.owner}'s bank account"

    def __set_pin(self, pincode):
        self.__pin = pincode

    def __get_pin(self):
        return self.__pin

    def __get_balance(self, pincode):
        if self.__pin == pincode:
            return f"There are £{self.__balance} on your bank account"
        else:
            return f"Incorrect pin"

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount, pincode):
        if self.__pin == pincode:
            if self.__balance >= amount:
                self.__balance -= amount
            else:
                return f"No enough funds to withdraw £{amount}"
        else:
            return f"Incorrect pin"


account = BankAccount("Alex", "1234")
print(account)
print(account.owner)
print(account._BankAccount__get_pin())
account._BankAccount__set_pin("asdf")
print(account._BankAccount__get_pin())
print(account._BankAccount__get_balance("asdf"))
print(account._BankAccount__get_balance("asdfg"))

account.deposit(200.34)
print(account._BankAccount__get_balance("asdf"))

account.withdraw(100.34, "asdf")
print(account._BankAccount__get_balance("asdf"))

print(account.withdraw(1000, "asdf"))

print(account._BankAccount__get_balance("asdf"))


