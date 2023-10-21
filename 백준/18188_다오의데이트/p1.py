'''
백준 18188. 다오의 데이트
'''

import sys
input = sys.stdin.readline


def delta(alp):
    if alp == "W":
        return [-1, 0]
    elif alp == "A":
        return [0, -1]
    elif alp == "S":
        return [1, 0]
    elif alp == "D":
        return [0, 1]


h, w = map(int, input().split())
bubble = []
dao = []
for i in range(h):
    line = input().split()
    if "D" in line[0]:
        dao = [i, line[0].index("D")]
    bubble.append(*line)
n = int(input())
case = [input().split() for _ in range(n)]


def find_way(nx, ny, i=0, ans=""):
    global answer
    if bubble[nx][ny] == "Z":
        answer = ans
        return
    if i == n:
        return
    for way in case[i]:
        x, y = delta(way)
        if 0 <= nx + x < h and 0 <= ny + y < w and bubble[nx + x][ny + y] != "@":
            find_way(nx + x, ny + y, i + 1, ans + way)


answer = ''
find_way(dao[0], dao[1])
possible = "YES" if answer else "NO"
print(possible, answer, sep="\n")