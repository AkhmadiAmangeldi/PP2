my_list = [4,7,9]

def histogram(my_list): 
    for i in my_list:
        for j in range(i):
            print("*", end = "")
        print()

histogram(my_list)