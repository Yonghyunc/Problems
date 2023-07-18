from collections import deque

n, m, t = map(int, input().split())
castle = []
gram = []
for l in range(n):
    line = list(map(int, input().split()))
    if line.count(2):
        gram = [l, line.index(2)]
    castle.append(line)

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]


visited = [[0] * m for _ in range(n)]
que = deque([[0, 0, 0]])
visited[0][0] += 1

gram_to_princess = (n - 1 - gram[0]) + (m - 1 - gram[1])
gram_way = 1e9
normal_way = 1e9
while que:
    x, y, time = que.popleft()
    if x == n - 1 and y == m - 1:
        normal_way = min(normal_way, time)
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if not castle[nx][ny]:
                visited[nx][ny] += 1
                que.append([nx, ny, time + 1])
            elif castle[nx][ny] == 2:
                gram_way = min(gram_way, time + 1)

min_way = min(normal_way, gram_way + gram_to_princess)
if min_way <= t:
    print(min_way)
else:
    print("Fail")

