from itertools import combinations
from collections import deque
from copy import deepcopy

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n, m = map(int, input().split())
arr = []
spot = []
blank = 0
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 2:
            spot.append([i, j, 1])
            line[j] = -1
        elif line[j] == 1:
            line[j] = -2
        elif not line[j]:
            blank += 1
    arr.append(line)

min_time = 1e9

for case in combinations(spot, m):
    new_arr = deepcopy(arr)
    for x, y, t in case:
        new_arr[x][y] = 1
    virus = deque(case)
    case_blank = blank
    last_virus = len(spot) - m
    max_time = 0
    while virus:
        x, y, t = virus.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not new_arr[nx][ny] or new_arr[nx][ny] == -1:
                    if not new_arr[nx][ny]:
                        case_blank -= 1
                    else:
                        last_virus -= 1
                    new_arr[nx][ny] = t + 1
                    max_time = t
                    virus.append([nx, ny, t + 1])
    if not case_blank and not last_virus:
        min_time = min(min_time, max_time)
if min_time == 1e9:
    min_time = -1
print(min_time)