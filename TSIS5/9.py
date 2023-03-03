import re

x = input()

space = re.sub(r'(?<=\w)([A-Z])', r' \1', x)

print(space)