# https://open.kattis.com/problems/bubbletea
import math

contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)
