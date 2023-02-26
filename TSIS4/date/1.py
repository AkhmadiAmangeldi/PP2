import datetime

today= datetime.date.today()

x=datetime.timedelta(5)

res=today-x

print("Current date:", today)
print("Subtracted date:", res)