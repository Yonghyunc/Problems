from itertools import combinations

n = int(input())
power = [list(map(int, input().split())) for _ in range(n)]

team = []
for i in range(1, n):
    team += list(combinations(list(range(0, n)), i))

min_diff = 1e9

for i in range(len(team) // 2):
    start = team[i]
    link = team[-(i + 1)]

    start_val = 0
    link_val = 0

    for a, b in combinations(start, 2):
        start_val += power[a][b] + power[b][a]

    for c, d in combinations(link, 2):
        link_val += power[c][d] + power[d][c]

    diff = abs(start_val - link_val)
    min_diff = min(min_diff, diff)

print(min_diff)