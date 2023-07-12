import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque


n = int(input())    # 보드의 크기
k = int(input())    # 사과의 개수
board = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1


l = int(input())    # 방향 변환 정보
change = deque([])
for _ in range(l):
    x, c = input().split()
    change.append([int(x), c])


board[0][0] = -1
snake = deque([[0, 0]])
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]      # 우 하 좌 상


def dummy(x, y, time=1, d=0):
    # 종료 조건 : 벽에 닿을 때 OR 뱀에 닿을 때
    if not 0 <= x < n or not 0 <= y < n or board[x][y] == -1:
        print(time)
        return

    # 사과 X
    if not board[x][y]:
        tx, ty = snake.popleft()
        board[tx][ty] = 0

    # 뱀 이동
    board[x][y] = -1
    snake.append([x, y])

    # 방향 바꾸기
    if change and time == change[0][0]:
        t, c = change.popleft()
        if c == "L":    # 왼쪽
            d = (d - 1) % 4
        elif c == "D":  # 오른쪽
            d = (d + 1) % 4
    # 게임 계속 진행
    dummy(x + delta[d][0], y + delta[d][1], time + 1, d)


dummy(0, 1)