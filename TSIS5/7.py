import re

def f(l):
    return l.group("g2").upper()

text = "my_super_var"

pattern = "(?P<g1>[_])(?P<g2>[a-z])"

print(re.sub(pattern, f, text))
