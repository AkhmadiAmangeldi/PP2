string = input()

def palindrome(string):
    s = string[::-1]
    if(s == string):
        return True
    return False
print(palindrome(string))