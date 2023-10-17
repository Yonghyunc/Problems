'''
백준 2146. 다리만들기

53% 시간초과
pypy로 하면 통과

대륙 내부의 좌표들은 딕셔너리에 추가하지 않도록 함
'''

import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
group = {}
nations = 0
answer = 1e9


def find_group(x, y, num):
    queue = deque([[x, y]])
    while queue:
        x, y = queue.popleft()
        is_inner = 0
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 2
                    queue.append([nx, ny])
                    is_inner += 1
                elif arr[nx][ny] == 2:
                    is_inner += 1
            else:
                is_inner += 1
        if is_inner != 4:
            group[num].append([x, y])


# 그룹화 (대륙별 좌표)
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            nations += 1
            group[nations] = []
            arr[i][j] = 2
            find_group(i, j, nations)


# 두 대륙씩 골라서 최소거리 구함 (맨해튼 거리 - 1)
for case in combinations(range(1, nations + 1), 2):
    group_a = group[case[0]]
    group_b = group[case[1]]
    for ax, ay in group_a:
        for bx, by in group_b:
            dis = abs(ax - bx) + abs(ay - by)
            answer = min(answer, dis)
print(answer - 1)