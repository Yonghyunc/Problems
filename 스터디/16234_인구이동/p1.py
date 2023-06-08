import sys
input = sys.stdin.readline
from collections import deque


n, l, r = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(n)]

delta = [(0, -1), (-1, 0), (0, 1), (1, 0)]

answer = 0

while True:

    groups = [[0] * n for _ in range(n)]
    g_num = 0
    populations = [0]
    unites = [0]

    # 1. 국경 열기
    for i in range(n):
        for j in range(n):
            queue = deque([])
            if not groups[i][j]:
                g_num += 1
                groups[i][j] = g_num
                populations.append(nations[i][j])
                unites.append(1)
                queue.append([i, j])
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in delta:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            if not groups[nx][ny] and l <= abs(nations[x][y] - nations[nx][ny]) <= r:
                                queue.append([nx, ny])
                                populations[g_num] += nations[nx][ny]
                                unites[g_num] += 1
                                groups[nx][ny] = g_num

    # 2. 인구 수 구하기
    is_possible = False
    calculated = [0] * len(unites)
    for g in range(1, len(unites)):
        calculated[g] += populations[g] // unites[g]
        if unites[g] > 1:
            is_possible = True

    if not is_possible:
        print(answer)
        break

    # 3. 인구 수 할당하기
    for i in range(n):
        for j in range(n):
            if groups[i][j] > 0:
                nations[i][j] = calculated[groups[i][j]]

    answer += 1