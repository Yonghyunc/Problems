import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())
condo = [[0] * m for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    condo[x - 1][y - 1] += 1

delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
max_trash = 0

for i in range(n):
    for j in range(m):
        if condo[i][j]:
            trash = 1
            condo[i][j] -= 1
            bundle = deque([[i, j]])
            while bundle:
                x, y = bundle.popleft()
                for dx, dy in delta:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and condo[nx][ny]:
                        bundle.append([nx, ny])
                        trash += 1
                        condo[nx][ny] -= 1
            max_trash = max(max_trash, trash)
print(max_trash)
