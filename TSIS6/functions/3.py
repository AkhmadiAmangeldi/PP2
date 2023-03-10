string = input()

rv = reversed(string)

def rvs(rv):
    for x in rv:
        return x

for q in string:
    if rvs(rv) == q:
        res = "YES"
    else:
        res = "NO"
        break

print(res)