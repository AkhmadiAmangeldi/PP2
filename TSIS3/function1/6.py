s = "python we are ready"

def reverse(s):
    s = s.split(" ")
    t = list(s)
    t.reverse()
    for i in t:
        print(i, end = ' ')
        
print(reverse(s))
