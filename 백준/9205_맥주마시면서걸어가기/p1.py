'''
3% 시간초과
'''

import sys
input = sys.stdin.readline
from collections import deque


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


tc = int(input())
for _ in range(tc):
    n = int(input())
    home = list(map(int, input().split()))
    cvs = []
    for _ in range(n):
        cvs.append(list(map(int, input().split())))
    goal = list(map(int, input().split()))

    spots = deque([])
    spots.append([home, []])
    emotion = "sad"

    while spots:
        now, visited = spots.popleft()
        if manhattan(now, goal) <= 1000:
            emotion = "happy"
            break
        for idx, coord in enumerate(cvs):
            if idx not in visited and manhattan(now, coord) <= 1000:
                spots.append([coord, visited + [idx]])
    print(emotion)