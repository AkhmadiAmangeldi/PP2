def true_false(q):
    return all(q)

list = []

for x in range(3):
    x = input()
    list.append(x)

x = tuple(list)

print(x)

print(true_false(x))