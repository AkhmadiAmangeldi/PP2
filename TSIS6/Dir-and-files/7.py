import os
os.chdir('C:/Users/Akhmadi/OneDrive/Рабочий стол/git/TSIS6/Dir-and-files')
f1 = open('file.txt', 'r')

for x in f1:
    f2 = open('file2.txt', 'w')
    final = f2.write(x)

#ready