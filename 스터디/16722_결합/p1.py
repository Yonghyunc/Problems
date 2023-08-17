import sys
input = sys.stdin.readline
from itertools import combinations

cards = [[] for _ in range(10)]
for i in range(1, 10):
    s, c, b = input().split()
    s = 0 if s == "CIRCLE" else (1 if s == "TRIANGLE" else 2)
    c = 0 if c == "YELLOW" else (1 if c == "RED" else 2)
    b = 0 if b == "GRAY" else (1 if b == "WHITE" else 2)
    cards[i] = [s, c, b]

success = []
gyeol = False
score = 0


def checking(a, b, c):
    three = [0, 0, 0]
    for i in range(3):
        turn = [0, 0, 0]
        for t in [a, b, c]:
            turn[cards[t][i]] += 1
        if turn.count(3) or not turn.count(0):
            three[i] += 1
        else:
            return
    success.append([a, b, c])


for case in combinations(range(1, 10), 3):
    checking(*case)


n = int(input())
for _ in range(n):
    commend, *nums = input().split()
    if commend == "H":
        nums = sorted(list(map(int, nums)))
        if nums in success:
            score += 1
            success.remove(nums)
        else:
            score -= 1

    if commend == "G":
        if not success and not gyeol:
            score += 3
            gyeol = True
        else:
            score -= 1

print(score)