# https://open.kattis.com/problems/height

num = int(input())

def insertionsort( aList ):
  for i in range( 1, len( aList ) ):
    tmp = aList[i]
    k = i
    while k > 0 and tmp < aList[k - 1]:
        aList[k] = aList[k - 1]
        k -= 1
    aList[k] = tmp

for j in range(num):
    a = input()
    times = insertionsort(a.split())
    print(j + " " + times)
