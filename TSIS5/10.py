import re

x = input()

symbol = re.sub(r'(?<=[a-z])([A-Z])', r'_\2', x)
print(symbol)
def snake(symbol):
    return re.sub(r'[A-Z]', lambda match : match.group().lower(), symbol)


print(snake(symbol))