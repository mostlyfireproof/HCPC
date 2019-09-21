# https://open.kattis.com/problems/semafori

data = input().split()

lines = int(data[0])
length = int(data[1])

lights = []
for i in range(lines):
    lights.append(input().split())

time = 0
lightsPassed = 0

for x in range(0, length):
    if x == lights[lightsPassed]:
        cycle = lights[1 + lightsPassed] + lights[2 + lightsPassed]
        while (time % cycle) >= lights[1 + lightsPassed]:
            time += 1
        lightsPassed += 3
    time += 1


print(time)
