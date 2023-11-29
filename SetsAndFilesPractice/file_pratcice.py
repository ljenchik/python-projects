with open('text.txt', 'r') as file:
    print(file.read())
print("**********************")

with open('text.txt', 'r') as file:
    print(file.readline())
print("**********************")

with open('text.txt', 'r') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())
print("**********************")

with open('text.txt', 'r') as file:
    print(file.readline(5))
    print(file.readline(5))
    print(file.readline(5))
    print(file.readline(5))
    print(file.readline(5))
print("**********************")


with open('text.txt', 'r') as file:
    f = file.readlines()
    print(list(f))

print("**********************")

with open('text.txt', 'r') as file:
    for line in file.readlines():
        print(line.strip())


print("**********************")

with open('text.txt', 'w') as file:
    file.write('Spaniel\n')

dogs = ["Cocker", "Cockapoo"]
with open('text.txt', 'w') as file:
    for dog in dogs:
        file.writelines(dog + "\n")
