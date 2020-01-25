# https://open.kattis.com/problems/egypt

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
        else:
            break

for j in range(0, (len(lines) - 1)):
    data = lines[j].split()
    if ((int(data[0]) * int(data[0]) + int(data[1]) * int(data[1])) == int(data[2]) * int(data[2])):
        print("right")
    else:
        print("wrong")
