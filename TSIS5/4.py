import re

x = input()

pattern = re.compile("^[A-Z]{1}[a-z]+")

result = re.search(pattern, x)

print(result)