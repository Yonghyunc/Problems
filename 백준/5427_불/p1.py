import sys
input = sys.stdin.readline
from collections import deque

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
tc = int(input())
for _ in range(tc):
    w, h = map(int, input().split())
    building = [[] for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    fire = deque()
    sg = deque()
    for i in range(h):
        line = input()
        for j in range(w):
            if line[j] == "@":
                sg.append([i, j, 0])
                visited[i][j] += 1
            elif line[j] == "*":
                fire.append([i, j, 0])
            building[i].append(line[j])

    second = 0
    fast_time = 0

    while sg or fire:
        if fast_time:
            break

        # 불의 번짐
        while fire and fire[0][2] == second:
            x, y, time = fire.popleft()
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and building[nx][ny] in [".", "@"]:
                    fire.append([nx, ny, time + 1])
                    building[nx][ny] = "*"

        # 상근이의 이동
        while sg and sg[0][2] == second:
            x, y, time = sg.popleft()
            for dx, dy in delta:
                sx, sy = x + dx, y + dy
                if sx >= h or sx < 0 or sy >= w or sy < 0:
                    fast_time = time + 1
                    break
                if 0 <= sx < h and 0 <= sy < w and building[sx][sy] == "." and not visited[sx][sy]:
                    sg.append([sx, sy, time + 1])
                    visited[sx][sy] += 1

        second += 1

    print(fast_time if fast_time else "IMPOSSIBLE")