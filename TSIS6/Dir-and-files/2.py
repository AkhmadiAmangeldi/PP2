import os
os.chdir('C:/Users/Akhmadi/OneDrive/Рабочий стол/git')
x = input()

if os.path.exists(x):
    print("exists")
else:
    print("does not exist")
    exit()

if os.access(x, os.R_OK):
    print("readable")
else:
    print("not readable")

if os.access(x, os.W_OK):
    print("writable")
else:
    print("not writable")

if os.access(x, os.X_OK):
    print("executable")
else:
    print("not executable")
#ready