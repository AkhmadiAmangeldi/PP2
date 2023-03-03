import re

x = input()

la = re.sub('\W', '..', x)

print(la)