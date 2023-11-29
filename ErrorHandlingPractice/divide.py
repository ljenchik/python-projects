import pdb
def divide(a, b):
    try:
        result = a /b
        return result
    except ZeroDivisionError:
        print("Don't divide by zero")
    except TypeError as err:
        print(err)
    else:
        print(f"{a} divided by {b} is equal {result}")

print(divide(2, 5))
pdb.set_trace()
print(divide(2, 0))
print(divide(2, 'a'))


def divide(a,b):
    try:
        total = a / b
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total
