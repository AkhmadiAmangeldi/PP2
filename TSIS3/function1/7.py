def has__33(lst):
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1] == 3:
            return True
    return False


l = list()
print("Enter size of list:")
n = int(input())
print("Enter elements of list:")
l = list(map(int, input().split()))
print(has__33(l))