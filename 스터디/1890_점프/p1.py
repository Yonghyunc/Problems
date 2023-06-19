# 시간초과

import sys
input = sys.stdin.readline

n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]


def dfs(x, y):
    move = game[x][y]
    visited[x][y] += 1
    print(x, y)
    if x == n - 1 and y == n - 1:
        print('--------')
        print(dp)
        print('-----------')
        return

    # 오른쪽으로 이동
    if x + move < n:
        dp[x + move][y] += dp[x][y]
        dfs(x + move, y)
    if y + move < n:
        dp[x][y + move] += dp[x][y]
        dfs(x, y + move)


dp[0][0] = 1
visited[0][0] = 1
dfs(0, 0)
print(dp[n - 1][n - 1])
print(visited)