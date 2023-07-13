# 83점

def what_number(idx, a, b, c):
    if idx <= a:
        return 0
    if a < idx <= a + b:
        return 1
    if a + b < idx <= a + b + c:
        return 2


m, n = map(int, input().split())
honeycomb = [[1] * m for _ in range(m)]
for _ in range(n):
    a, b, c = map(int, input().split())
    for d in range(2 * m - 1):
        if d < m:
            honeycomb[m - d - 1][0] += what_number(d + 1, a, b, c)
        else:
            honeycomb[0][d - m + 1] += what_number(d + 1, a, b, c)

for i in range(1, m):
    for j in range(1, m):
        honeycomb[i][j] = max(honeycomb[i - 1][j], honeycomb[i][j - 1])

for i in range(m):
    print(*honeycomb[i])