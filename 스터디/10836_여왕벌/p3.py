import sys
input = sys.stdin.readline

m, n = map(int, input().split())
honeycomb = [1] * (2 * m - 1)

for _ in range(n):
    day = list(map(int, input().split()))
    idx = 0
    for i in range(3):
        for j in range(idx, idx + day[i]):
            honeycomb[j] += i
        idx += day[i]

print(*honeycomb[m - 1:])
for i in range(m - 2, -1, -1):
    print(honeycomb[i], *honeycomb[m:])