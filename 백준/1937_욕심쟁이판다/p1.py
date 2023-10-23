'''
백준 1937. 욕심쟁이 판다
BFS + DP
34% 시간초과
'''

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = [[0] * n for _ in range(n)]
max_dis = 0


def checking(x, y, val, dis):
    if 0 <= x < n and 0 <= y < n and forest[x][y] > val and dis > visited[x][y]:
        return True
    else:
        return False


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = 1
            que = deque([])
            que.append([i, j])
            while que:
                x, y = que.popleft()
                now = forest[x][y]
                dis = visited[x][y]
                max_dis = max(max_dis, dis)
                for dx, dy in delta:
                    nx, ny = x + dx, y + dy
                    if checking(nx, ny, now, dis + 1):
                        visited[nx][ny] = dis + 1
                        que.append([nx, ny])

print(max_dis)