from itertools import combinations
from copy import deepcopy

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, input().split())
arr = []
blank = []
first_blank = 0
virus = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if not line[j]:
            blank.append([i, j])
            first_blank += 1
        elif line[j] == 2:
            virus.append([i, j])
    arr.append(line)


def spread_virus(x, y):
    global blank_cnt
    if blank_cnt <= max_blank:
        return
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if not new_arr[nx][ny]:
                blank_cnt -= 1
                new_arr[nx][ny] = 3
                spread_virus(nx, ny)


max_blank = 0
for case in combinations(blank, 3):
    new_arr = deepcopy(arr)
    for cx, cy in case:
        new_arr[cx][cy] = 1
    blank_cnt = first_blank - 3
    for x, y in virus:
        spread_virus(x, y)
    max_blank = max(max_blank, blank_cnt)
print(max_blank)