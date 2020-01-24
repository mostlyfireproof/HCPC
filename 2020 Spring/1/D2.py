# https://open.kattis.com/problems/datum
from datetime import date

inp = input()
a = inp.split()

d = int(a[0])
m = int(a[1])

base = date(2009, 1, 1)

q = date(2009, m, d)

dayOfYear = (q - base).days

if dayOfYear % 7 == 0:
    print("Thursday")
elif dayOfYear % 7 == 1:
    print("Friday")
elif dayOfYear % 7 == 2:
    print("Saturday")
elif dayOfYear % 7 == 3:
    print("Sunday")
elif dayOfYear % 7 == 4:
    print("Monday")
elif dayOfYear % 7 == 5:
    print("Tuesday")
elif dayOfYear % 7 == 6:
    print("Wednesday")
