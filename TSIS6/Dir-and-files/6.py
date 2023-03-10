import os
import string 

x = string.ascii_uppercase

for letter in x:
    z = letter + '.txt'
    with open(z, 'x') as file:
        file.write(" ")
        file.close()