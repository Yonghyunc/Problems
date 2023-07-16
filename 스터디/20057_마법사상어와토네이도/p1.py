from math import trunc

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
x, y = n // 2, n // 2
delta = [(0, -1, 0), (1, 0, 0), (0, 1, 1), (-1, 0, 1)]
move = [(0, 2, 0.05), (1, 1, 0.1), (-1, 1, 0.1), (2, 0, 0.02), (-2, 0, 0.02),
        (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.01), (-1, -1, 0.01)]
outside = 0

for turn in range(1, n + 1, 2):
    for dx, dy, t in delta:
        t += turn
        while t:
            x, y = x + dx, y + dy
            t -= 1
            if 0 <= x < n and 0 <= y < n:
                sand = board[x][y]
                for i in range(9):
                    if not dx:  # 왼, 오
                        nx, ny = x + move[i][0] * dy, y + move[i][1] * dy
                    else:
                        nx, ny = x + move[i][1] * dx, y + move[i][0] * dx
                    blow = trunc(board[x][y] * move[i][2])
                    sand -= blow
                    if 0 <= nx < n and 0 <= ny < n:
                        board[nx][ny] += blow
                    else:
                        outside += blow
                board[x][y] = 0

                if 0 <= x + dx < n and 0 <= y + dy < n:
                    board[x + dx][y + dy] += sand
                else:
                    outside += sand

print(outside)



