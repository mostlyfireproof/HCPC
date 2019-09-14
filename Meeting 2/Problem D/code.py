# https://open.kattis.com/problems/licensetolaunch

line1 = input()
line2 = input()

data = line2.split()
data = [int(i) for i in data]

print((data.index(min(data))))
