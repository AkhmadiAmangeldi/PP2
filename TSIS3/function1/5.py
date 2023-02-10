def permute(data, i, length):
    if i == length:
        print(''.join(data))
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permute(data, i+1, length)
            data[i], data[j] = data[j], data[i]

def all_permutations(string):
    permute(list(string), 0, len(string))

string = input()
all_permutations(string)