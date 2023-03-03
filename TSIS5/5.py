import re

x = input()

pattern = re.compile(".*[a].*[b]$")

result = re.search(pattern, x)

print(result)