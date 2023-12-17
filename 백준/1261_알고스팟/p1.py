import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
maze = [list(map(int, list(input().rstrip()))) for _ in range(m)]
visited = [[-1] * n for _ in range(m)]
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

location = []
heapq.heappush(location, [0, 0, 0])
visited[0][0] = 0

while location:
    wall, x, y = heapq.heappop(location)
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == -1:
            if not maze[nx][ny]:
                visited[nx][ny] = wall
                heapq.heappush(location, [wall, nx, ny])
            else:
                visited[nx][ny] = wall + 1
                heapq.heappush(location, [wall + 1, nx, ny])
print(visited[-1][-1])
