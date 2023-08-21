import sys
input = sys.stdin.readline
from collections import deque

n, m, t = map(int, input().split())
circle = [list(map(int, input().split())) for _ in range(n)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def rotate(num, d, k):
    line = circle[num][::]
    if d == 0:
        new = line[m - k:] + line[:m - k]
    else:
        new = line[k:] + line[:k]
    circle[num] = new


def erase(x, y):
    num = circle[x][y]
    circle[x][y] = 0
    line_close = 0
    queue = deque([])
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and -1 <= ny <= m:
                ny = 0 if ny == m else ny
                ny = m - 1 if ny == -1 else ny
                if circle[nx][ny] == num:
                    line_close = 1
                    circle[nx][ny] = 0
                    queue.append([nx, ny])
    circle[x][y] = 0 if line_close else num
    return line_close


def get_avg():
    sum_circle = 0
    cnt = n * m
    for i in range(n):
        sum_circle += sum(circle[i])
        cnt -= circle[i].count(0)
    if cnt:
        return sum_circle / cnt
    else:
        return 0



def get_sum():
    sum_circle = 0
    for i in range(n):
        sum_circle += sum(circle[i])
    return sum_circle


for _ in range(t):
    x, d, k = map(int, input().split())

    for num in range(x - 1, n, x):
        rotate(num, d, k)

    close = 0
    for i in range(n):
        for j in range(m):
            if circle[i][j]:
                close += erase(i, j)

    if not close:
        avg = get_avg()
        for i in range(n):
            for j in range(m):
                if circle[i][j]:
                    if circle[i][j] > avg:
                        circle[i][j] -= 1
                    elif circle[i][j] < avg:
                        circle[i][j] += 1


print(get_sum())