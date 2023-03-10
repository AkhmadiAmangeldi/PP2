import os
os.chdir('C:/Users/Akhmadi/OneDrive/Рабочий стол/git/TSIS6/Dir-and-files')
with open('file.txt') as line:
    count = 0
    for x in line:
        count += 1
        print(count)