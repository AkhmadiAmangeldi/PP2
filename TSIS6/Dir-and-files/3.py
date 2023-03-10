import os
os.chdir('C:/Users/Akhmadi/OneDrive/Рабочий стол/git')
print(os.getcwd())

x = input()

if os.path.exists(x):
    print(True)
else:
    print(False)
#ready