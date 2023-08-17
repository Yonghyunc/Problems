import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dis = [0] * m
delta = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
remain = m

x, y = map(int, input().split())
for i in range(m):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = i + 1

queue = deque([[x - 1, y - 1, 0]])
visited[x - 1][y - 1] += 1
while m and queue:
    x, y, t = queue.popleft()
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] += 1
            queue.append([nx, ny, t + 1])
            if board[nx][ny]:
                dis[board[nx][ny] - 1] = t + 1
                remain -= 1

print(*dis)

