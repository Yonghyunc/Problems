# https://www.acmicpc.net/problem/2667


from collections import deque

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
deq = deque()


def complex(x, y):
    deq.append([x, y])
    visited[x][y] = 1
    cnt = 1
    while deq:
        x, y = deq.popleft()
        for d in range(4):
            nx = x + delta[d][0]
            ny = y + delta[d][1]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and arr[nx][ny] == '1':
                    deq.append([nx, ny])
                    visited[nx][ny] = 1
                    cnt += 1
    com_cnt.append(cnt)



n = int(input())
arr = [input() for _ in range(n)]
visited = [[0] * n for _ in range(n)]
com_num = 0
com_cnt = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == '1' and not visited[i][j]:
            complex(i, j)
            com_num += 1

print(com_num)
com_cnt.sort()
for i in range(len(com_cnt)):
    print(com_cnt[i])