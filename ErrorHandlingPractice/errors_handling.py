# SyntaxError : invalid syntax
# NameError : variable is not defined
# TypeError : mismatch of data types
# IndexError
# ValueError
# KeyError : no key in dictionary
# AttributeError : object does not have attribute (method)

try:
    foobar
except NameError as error:
    print(error)

d = {"name": "Lo"}

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

print(get(d, "name"))
print(get(d, "city"))

try:
    num = int(input("Enter a number: "))
except:
    print("It's not a number")
else: # runs if except does not run
    print("All good!")
finally: # always runs
    print("Always!")



while True:
    try:
        num = int(input("Enter a number: "))
    except:
        print("It's not a number")
    else: # runs if except does not run
        print("All good!")
        break
    finally: # always runs
        print("Always!")

