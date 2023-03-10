import math

list = []

for x in range(5):
    x = int(input())
    list.append(x)

result = math.prod(list)
print(result)