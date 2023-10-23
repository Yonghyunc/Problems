'''
백준 1937. 욕심쟁이 판다
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dp = [[-1] * n for _ in range(n)]
max_dis = 0


def dfs(x, y):
    if dp[x][y] == -1:
        dp[x][y] = 0
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and forest[nx][ny] > forest[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny))
    return dp[x][y] + 1


for i in range(n):
    for j in range(n):
        max_dis = max(max_dis, dfs(i, j))
print(max_dis)