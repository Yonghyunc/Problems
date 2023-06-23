import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
lab = [[] for _ in range(n)]
virus = []
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
min_time = 1e9
blank = 0

# 빈 칸(0) / 벽(|) / 비활성 바이러스(-1)
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            lab[i].append('|')
        elif line[j] == 2:
            lab[i].append(-1)
            virus.append([i, j, 0])
        else:
            lab[i].append(0)
            blank += 1
# 빈 칸이 애초에 없으면
if not blank:
    print(0)
else:
    for case in combinations(virus, m):
        room = deque(list(case))
        new_lab = copy.deepcopy(lab)                # 깊은 복사 (이중 배열)
        new_blank = blank
        # 최소 시간 구하기
        time = 0
        while room:
            x, y, t = room.popleft()
            if new_lab[x][y] != "*":
                time = max(time, t)
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if new_lab[nx][ny] == "|":
                        pass
                    elif not new_lab[nx][ny]:
                        new_lab[nx][ny] = t + 1
                        room.append([nx, ny, new_lab[nx][ny]])
                        new_blank -= 1
                    elif new_lab[nx][ny] == -1:
                        new_lab[nx][ny] = "*"
                        room.append([nx, ny, t + 1])

        # 빈 칸 확인하기
        if not new_blank:
            min_time = min(min_time, time)

    if min_time == 1e9:
        min_time = -1
    print(min_time)



