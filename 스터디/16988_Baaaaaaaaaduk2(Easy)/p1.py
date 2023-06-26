import sys
input = sys.stdin.readline
from itertools import combinations


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, input().split())
board = []
blank = []
for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(m):
        if not line[j]:
            blank.append([i, j])

check = []
for bx, by in blank:
    isSatisfied = False
    for dx, dy in delta:
        if 0 <= bx + dx < n and 0 <= by + dy < m:
            if board[bx + dx][by + dy] == 2:
                isSatisfied = True
    if isSatisfied:
        check.append([bx, by])


def beside(x, y):
    for dx, dy in delta:
        if 0 <= x + dx < n and 0 <= y + dy < m:
            if board[x + dx][y + dy] == 2:
                bes.append([x + dx, y + dy])


def baduk(x, y):
    global isChanged, cnt
    visited[x][y] = 1
    cnt += 1
    for dx, dy in delta:
        if 0 <= x + dx < n and 0 <= y + dy < m:
            if not visited[x + dx][y + dy] and board[x + dx][y + dy] == 2:
                baduk(x + dx, y + dy)
            elif not board[x + dx][y + dy]:
                isChanged = False

max_cnt = 0

if len(check) == 1:
    nx, ny = check.pop()
    board[nx][ny] = 1
    visited = [[0] * m for _ in range(n)]
    all_cnt = 0
    bes = []
    beside(nx, ny)
    for bx, by in bes:
        isChanged = True
        cnt = 0
        if not visited[bx][by]:
            baduk(bx, by)
            if isChanged:
                all_cnt += cnt
    max_cnt = max(max_cnt, all_cnt)

for case in combinations(check, 2):
    for cx, cy in case:
        board[cx][cy] = 1
    visited = [[0] * m for _ in range(n)]
    all_cnt = 0
    bes = []
    for cx, cy in case:
        beside(cx, cy)
    for bx, by in bes:
        isChanged = True
        cnt = 0
        if not visited[bx][by]:
            baduk(bx, by)
            if isChanged:
                all_cnt += cnt
    for cx, cy in case:
        board[cx][cy] = 0
    max_cnt = max(max_cnt, all_cnt)

print(max_cnt)