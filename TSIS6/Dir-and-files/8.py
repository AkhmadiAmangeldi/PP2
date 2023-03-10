import os
os.chdir('C:/Users/Akhmadi/OneDrive/Рабочий стол/git/TSIS6/Dir-and-files')
x = input()
if os.path.exists(x):
    di = input()
    os.rmdir(di)
else:
    print('Path is didnt exists')