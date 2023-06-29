import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
results = [list(map(int, input().split())) for _ in range(n)]
max_score = 0

for case in permutations(range(1, 9), 8):
    batting_order = list(case[:3]) + [0] + list(case[3:])
    base = [0, 0, 0]     # 베이스 상황
    out_count = 0
    inning = 1
    score = 0

    while inning <= n:
        player = batting_order.pop(0)
        hit = results[inning - 1][player]
        if hit == 0:        # 아웃일 경우
            out_count += 1
            if out_count == 3:
                inning += 1
                out_count = 0
                base = [0, 0, 0]
        elif hit == 1:
            new_base = [1, 0, 0]
            if base[-1] == 1:
                score += 1
            for b in range(2):
                new_base[b + 1] = base[b]
            base = new_base
        elif hit == 2:
            score += base[1] + base[2]
            base = [0, 1, 0]
            if base[0]:
                base[2] = 1
        else:
            score += base[0] + base[1] + base[2]
            if hit == 3:
                base = [0, 0, 1]
            elif hit == 4:
                score += 1
                base = [0, 0, 0]

        # 치고 나서는 다시 타순 끝에 넣어줌
        batting_order.append(player)
    max_score = max(score, max_score)

print(max_score)