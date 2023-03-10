import time
import math

sqrt = int(input())
timing = int(input())

time.sleep(timing / 1000)

res = math.sqrt(sqrt)

print(f"Square root of {sqrt} after {timing} miliseconds is {res}")