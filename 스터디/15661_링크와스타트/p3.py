# 비트연산자로 풀어보자!
from itertools import combinations


# 여기를 개선하면 더 빨라질 듯!
def get_score(team):
    value = 0
    for a, b in combinations(team, 2):
        value += power[a][b] + power[b][a]
    return value


n = int(input())
power = [list(map(int, input().split())) for _ in range(n)]
member = list(range(0, n))
new_power = []


min_diff = 1e9

start = []
link = []

for i in range(1, (1<<n) // 2):
    for j in range(n):
        if i&(1<<j):
            start.append(member[j])
        else:
            link.append(member[j])

    start_val = get_score(start)
    link_val = get_score(link)

    min_diff = min(min_diff, abs(start_val - link_val))

    start = []
    link = []

print(min_diff)

