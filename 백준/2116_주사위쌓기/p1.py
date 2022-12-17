# https://www.acmicpc.net/problem/2116

import copy
import sys

sys.setrecursionlimit(1000000)  # 런타임 에러를 방지하기 위해 최대 재귀 깊이를 늘려줌

# 0-5 / 1-3 / 2-4
pair = [5, 3, 4, 1, 2, 0]


def dice(x, top):
    global max_side
    now = copy.deepcopy(dices[x])              # 현재 주사위
    idx = pair[now.index(top)]
    new_top = now[idx]         # 윗면 (다음 주사위 아랫면)
    now.remove(top)
    now.remove(new_top)
    max_side += max(now)

    if x < n - 1:
        dice(x + 1, new_top)


n = int(input())            # 주사위 개수
dices = [list(map(int, input().split())) for _ in range(n)]
max_result = 0

for top_num in dices[0]:
    max_side = 0
    dice(0, top_num)
    if max_side > max_result:
        max_result = max_side
print(max_result)