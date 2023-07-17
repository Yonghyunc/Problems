import sys
input = sys.stdin.readline
from collections import deque

n, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2 ** n)]
steps = list(map(int, input().split()))
delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def rotate(l):
    part = 2 ** l
    for x in range(2 ** n // part):
        for y in range(2 ** n // part):
            part_board = []
            for j in range(y * part, y * part + part):
                part_line = []
                for i in range(x * part + part - 1, x * part - 1, -1):
                    part_line.append(board[i][j])
                part_board.append(part_line)
            for k in range(part):
                board[x * part + k][y * part: y * part + part] = part_board[k]


def check_ice(x, y):
    ice = 0
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n:
            if board[nx][ny]:
                ice += 1
            elif not board[nx][ny] and removed[nx][ny]:
                ice += 1
    if ice < 3:
        board[x][y] -= 1
        removed[x][y] += 1
        board[x][y] = max(0, board[x][y])


def find_block(i, j):
    global max_block
    block = 0
    visited[i][j] += 1
    que = deque([[i, j]])
    while que:
        x, y = que.popleft()
        block += 1
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n and board[nx][ny] and not visited[nx][ny]:
                que.append([nx, ny])
                visited[nx][ny] += 1
    max_block = max(max_block, block)


for step in steps:
    rotate(step)
    removed = [[0] * (2 ** n) for _ in range(2 ** n)]
    for i in range(2 ** n):
        for j in range(2 ** n):
            if board[i][j]:
                check_ice(i, j)

remain_ice = 0
max_block = 0
visited = [[0] * (2 ** n) for _ in range(2 ** n)]
for i in range(2 ** n):
    for j in range(2 ** n):
        remain_ice += board[i][j]
        if board[i][j] and not visited[i][j]:
            find_block(i, j)

print(remain_ice, max_block, sep="\n")