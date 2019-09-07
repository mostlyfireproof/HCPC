import math

var = input()

data = var.split()

bridges = int(data[0]) - 1
knights = int(data[1])
groupSize = int(data[2])

days = math.ceil(bridges / math.floor(knights / groupSize))

print(days)
