from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# dp[0][0] = 1


def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    ways = 0
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and board[x][y] > board[nx][ny]:
            ways += dfs(nx, ny)

    dp[x][y] = ways
    return dp[x][y]

print(dfs(0, 0))