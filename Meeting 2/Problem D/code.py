# https://open.kattis.com/problems/licensetolaunch
import math

line1 = input()
line2 = input()

data = line2.split()

print(data.index(min(data)))
