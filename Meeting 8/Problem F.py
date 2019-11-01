# https://open.kattis.com/problems/shopaholic

length = int(input())

priceList = input().split()

priceList = [int(i) for i in priceList]
priceList.sort()

thingsToBePaidFor = 0

for i in range(0, length):
    if 0 == (i % 3):
        thingsToBePaidFor += priceList[i]
    else:
        thingsToBePaidFor

print(thingsToBePaidFor)
