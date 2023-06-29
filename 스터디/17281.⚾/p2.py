import sys
input = sys.stdin.readline
from itertools import permutations

innings = int(input())
results = [list(map(int, input().split())) for _ in range(innings)]
max_score = 0

for case in permutations(range(1, 9), 8):
    batting_order = list(case[:3]) + [0] + list(case[3:])
    player = 0
    score = 0
    for inning in range(innings):
        outCount = 0
        base1, base2, base3 = 0, 0, 0
        while outCount < 3:
            hit = results[inning][batting_order[player]]
            if not hit:
                outCount += 1
            elif hit == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif hit == 2:
                score += (base2 + base3)
                base1, base2, base3 = 0, 1, base1
            elif hit == 3:
                score += (base1 + base2 + base3)
                base1, base2, base3 = 0, 0, 1
            elif hit == 4:
                score += (base1 + base2 + base3 + 1)
                base1, base2, base3 = 0, 0, 0
            if player == 8:
                player = 0
            else:
                player += 1
    max_score = max(max_score, score)
print(max_score)