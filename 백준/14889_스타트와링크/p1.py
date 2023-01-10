# https://www.acmicpc.net/problem/14889

from itertools import combinations

n = int(input())
power = [list(map(int, input().split())) for _ in range(n)]

team = list(combinations(list(range(1, n + 1)), n // 2))

min_diff = 10000

for i in range(len(team) // 2):
    start = team[i]
    link = team[-(i + 1)]
    start_val = 0
    link_val = 0
    for a, b in combinations(start, 2):
        start_val += power[a - 1][b - 1] + power[b - 1][a - 1]

    for c, d in combinations(link, 2):
        link_val += power[c - 1][d - 1] + power[d - 1][c - 1]

    diff = abs(start_val - link_val)
    if min_diff > diff:
        min_diff = diff

print(min_diff)

