'''
백준 14267. 회사 문화 1
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
boss = list(map(int, input().split()))
score = [0] * (n + 1)

for _ in range(m):
    employee, weight = map(int, input().split())
    score[employee] += weight

for emp_num, boss_num in enumerate(boss):
    emp_num += 1
    if emp_num > 1:
        score[emp_num] += score[boss_num]
print(*score[1:])