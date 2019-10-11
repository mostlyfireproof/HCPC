# https://open.kattis.com/problems/semafori

data = input().split()

lines = int(data[0])
length = int(data[1])

lightsRaw = []
for i in range(lines):
    lightsRaw.append(input().split())


lights = sum(lightsRaw, [])
for j in range(0, len(lights)):
    lights[j] = int(lights[j])

time = 0
lightsPassed = 0

for x in range(0, length):
    try:
        #print("lightspassed",lightsPassed)
        #print(x)
        #print("lights:", lights)
        if x == lights[lightsPassed]:
            #print("debug")
            cycle = lights[1 + lightsPassed] + lights[2 + lightsPassed]
            while (time % cycle) >= lights[2 + lightsPassed]:
                time += 1
            lightsPassed += 3
        time += 1
    except:
        pass
        
print(time)

#print(lights)
#print(lines)
#print(length)
#print(lightsPassed)
#print(time)
