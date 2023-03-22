# 백준 3055. 탈출

from collections import deque

r, c = map(int, input().split())
forest = [input() for _ in range(r)]

water = []
for i in range(r):
    for j in range(c):
        if forest[i][j] == '*':
            water.append([i, j])
        if forest[i][j] == 'S':
            hedgehog = (i, j)

flood = [[-1] * c for _ in range(r)]
move = [[-1] * c for _ in range(r)]

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def getFlood(water:list) -> None:
    '''
    몇 분만에 물이 차는지 구하는 함수
    '''
    que = deque()
    for x, y in water:
        que.append([x, y, 0])
        flood[x][y] = 0
    while que:
        x, y, cnt = que.popleft()
        for d in range(4):
            nx, ny = x + delta[d][0], y + delta[d][1]
            if 0 <= nx < r and 0 <= ny < c:
                if forest[nx][ny] not in ['X', 'D']:
                    if flood[nx][ny] == -1 or cnt + 1 < flood[nx][ny]:
                        flood[nx][ny] = cnt + 1
                        que.append([nx, ny, cnt + 1])


def moving(x:int, y:int) -> None:
    '''
    고슴도치를 이동시키는 함수
    '''
    que = deque()
    que.append([x, y, 0])
    move[x][y] = 0
    while que:
        x, y, cnt = que.popleft()
        for d in range(4):
            nx, ny = x + delta[d][0], y + delta[d][1]
            if 0 <= nx < r and 0 <= ny < c:
                if forest[nx][ny] == 'D':
                    return cnt + 1
                if forest[nx][ny] != 'X' and (cnt + 1 < flood[nx][ny] or flood[nx][ny] == -1):
                    if move[nx][ny] == -1 or cnt + 1 < move[nx][ny]:
                        move[nx][ny] = cnt + 1
                        que.append([nx, ny, cnt + 1])

                if not water and forest[nx][ny] != 'X':
                    if move[nx][ny] == -1 or cnt + 1 < move[nx][ny]:
                        move[nx][ny] = cnt + 1
                        que.append([nx, ny, cnt + 1])

    return 'KAKTUS'


getFlood(water)
print(moving(hedgehog[0], hedgehog[1]))

