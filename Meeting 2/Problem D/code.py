# https://open.kattis.com/problems/licensetolaunch

line1 = input()
line2 = input()

data = line2.split()

print(int(data.index(min(data))))
