# 시간초과

import sys
input = sys.stdin.readline

n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]


def dp(x, y):
    road = 0
    if x == 0 and y == 0:
        return 1
    for i in range(1, 10):
        if 0 <= x - i < n:
            if game[x - i][y] == i:
                road += dp(x - i, y)
        if 0 <= y - i < n:
            if game[x][y - i] == i:
                road += dp(x, y - i)
    return road

print(dp(n - 1, n - 1))