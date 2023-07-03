import sys
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
k_delta = [(-1, -2), (-2, -1), (1, -2), (2, -1), (-1, 2), (-2, 1), (1, 2), (2, 1)]
n, m = map(int, input().split())
board = [[0] * m for _ in range(n)]
blank = m * n
queen = []
knight = []
for i in range(3):
    line = list(map(int, input().split()))
    cnt = line[0]
    for j in range(1, len(line) // 2 + 1):
        x, y = line[j * 2 - 1] - 1, line[j * 2] - 1
        board[x][y] += 2
        blank -= 1
        if i == 0:      # queen
            queen.append([x, y])
        elif i == 1:    # knight
            knight.append([x, y])


def move_queen(x, y):
    global blank
    for dx, dy in delta:
        nx, ny = x, y
        while True:
            nx += dx
            ny += dy
            if 0 <= nx < n and 0 <= ny < m:
                if not board[nx][ny]:
                    board[nx][ny] += 1
                    blank -= 1
                elif board[nx][ny] == 2:
                    break
            else:
                break


def move_knight(x, y):
    global blank
    for dx, dy in k_delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if not board[nx][ny]:
                board[nx][ny] += 1
                blank -= 1


for qx, qy in queen:
    move_queen(qx, qy)
for kx, ky in knight:
    move_knight(kx, ky)

print(blank)