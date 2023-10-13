'''
백준 14923. 미로 탈출
BFS (x좌표, y좌표, 거리, 지팡이 사용 여부)
'''

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]

case = deque([])
case.append([sx - 1, sy - 1, 0, False])
visited[sx - 1][sy - 1] += 1
min_dis = 1e9
while case:
    x, y, d, cane = case.popleft()
    if x == ex - 1 and y == ey - 1:
        min_dis = min(min_dis, d)
    if d < min_dis:                         # 조건을 줄여주어 시간 초과 해결
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not maze[nx][ny]:
                    if not visited[nx][ny] or (not cane and visited[nx][ny] == 2):
                        visited[nx][ny] += 1 if not cane else 2
                        case.append([nx, ny, d + 1, cane])
                if maze[nx][ny] and not cane:
                    visited[nx][ny] += 2
                    case.append([nx, ny, d + 1, True])

if min_dis == 1e9:
    print(-1)
else:
    print(min_dis)