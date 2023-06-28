# https://www.acmicpc.net/problem/17086

delta = [[0, -1], [-1, 0], [0, 1], [1, 0], [-1, -1], [-1, 1], [1, 1], [1, -1]]


def move(x, y):
    global now
    nx, ny = x, y
    for d in range(8):
        nx += delta[d][0]
        ny += delta[d][1]
        if 0 <= nx < m and 0 <= ny < n:
            if distance[nx][ny] < now:
                distance[nx][ny] = now
        now += 1
        move(nx, ny)
        now -= 1




n, m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
distance = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if room[i][j] == 1:
            now = 1
            move(i, j)

print(distance)