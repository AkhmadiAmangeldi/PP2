import re

x = input()

la = re.search('a[b]*', x)

print(la)