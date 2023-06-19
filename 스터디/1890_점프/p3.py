n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

def fill(x, y):
    move = game[x][y]
    if x == n - 1 and y == n - 1:
        return
    if 0 <= x + move < n:
        dp[x + move][y] += dp[x][y]
    if 0 <= y + move < n:
        dp[x][y + move] += dp[x][y]


for i in range(n):
    for j in range(n):
        fill(i, j)

print(dp[n - 1][n - 1])