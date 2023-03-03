import re

x = input()

la = re.search(r'a[b]{2,3}', x)

print(la)

