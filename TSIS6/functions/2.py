x = input()

up_n = 0
low_n = 0

for char in x:
    if char.isupper():
        up_n += 1
    elif char.islower():
        low_n += 1

print(up_n, low_n)