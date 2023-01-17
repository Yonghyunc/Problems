# https://www.acmicpc.net/problem/13300

import math

n, k = map(int, input().split())
students = [[0] * 2 for _ in range(6)]

for _ in range(n):
    s, y = map(int, input().split())
    students[y - 1][s] += 1

result = 0

for i in range(6):
    for j in range(2):
        result += math.ceil(students[i][j] / k)

print(result)