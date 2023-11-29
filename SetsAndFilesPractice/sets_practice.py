l = [1, 2, 3, 3, 3, 5, 4, 8]
s = set(l)
print(type(s))
print(s)
f = frozenset(l)
print(f)
print(f.__hash__())
s = "hello"
print(s.__hash__())
s = 3
print(s.__hash__())
