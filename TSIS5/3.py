import re

x = input()

pattern = re.compile("[a-z]+_[a-z]+")

result = re.search(pattern, x)

print(result)