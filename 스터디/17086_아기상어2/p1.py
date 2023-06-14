n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

delta = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

sharks = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            sharks.append([i, j, 0])
            arr[i][j] = -1

max_dis = 0
while sharks:
    x, y, dis = sharks.pop()
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0 or arr[nx][ny] > dis + 1:
                arr[nx][ny] = dis + 1
                sharks.append([nx, ny, dis + 1])


for i in range(n):
    max_dis = max(*arr[i], max_dis)
print(max_dis)
