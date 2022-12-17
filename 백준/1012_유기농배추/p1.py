# https://www.acmicpc.net/problem/1012

import sys

sys.setrecursionlimit(10000)  # 런타임 에러를 방지하기 위해 최대 재귀 깊이를 늘려줌

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def dfs(x, y):
    visited[x][y] = 1

    for d in range(4):
        nx = x + delta[d][0]
        ny = y + delta[d][1]
        if 0 <= nx < m and 0 <= ny < n:
            if not visited[nx][ny] and ground[nx][ny] == 1:
                dfs(nx, ny)


for t in range(int(input())):
    m, n, k = map(int, input().split())
    ground = [[0] * n for _ in range(m)]
    visited = [[0] * n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        ground[x][y] = 1

    worm = 0
    for i in range(m):
        for j in range(n):
            if ground[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                worm += 1

    print(worm)


