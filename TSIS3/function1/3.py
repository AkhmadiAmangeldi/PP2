def solve(numheads, numlegs):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if (2 * chickens) + (4 * rabbits) == numlegs:
            return chickens, rabbits
    return None, None

numheads = int(input())
numlegs = int(input())
chickens, rabbits = solve(numheads, numlegs)

if chickens is not None and rabbits is not None:
    print(chickens , "chickens")
    print(rabbits , "rabbits")
else:
    print("No solution found")