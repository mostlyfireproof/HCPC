# https://open.kattis.com/problems/helpaphd

import math
problems = int(input())

maths = ""
for j in range(1,problems):
    maths+=input()+" "

data = maths.split()

for line in range(1, problems):
    if data[line] == "P=NP":
        print("skipped")
    else:
        heck = data[line].split('+')
        print(int(heck[0]) +int(heck[1]))
