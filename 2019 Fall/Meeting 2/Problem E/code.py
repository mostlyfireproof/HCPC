# https://open.kattis.com/problems/yinyangstones

rockCircle = input()

for x in range(0, len(rockCircle)):
    for y in range(0, len(rockCircle)):
        # test for B+1
            rockCircle = rockCircle[0:x] + 'B' + rockCircle[y:len(rockCircle)]
        # test for W+1
            rockCircle = rockCircle[0:x] + 'W' + rockCircle[y:len(rockCircle)]
