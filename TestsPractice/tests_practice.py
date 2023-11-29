# Assertions
def myFunction(a, b):
    assert a > 0 and b > 0, "Both numbers must be positive"
    return a + b


print(myFunction(1, 2))


# print(myFunction(1, -2))
def eat(food):
    assert food in ['pizza', 'ice cream', 'candy'], "Food must be junk"
    return "Yuamm"


# print(eat("bread"))

def largest(l):
    try:
        return max(l)
    except TypeError:
        return "You should pass a list of numbers"

def is_funny(name):
    return True
