import sys
input = sys.stdin.readline
from collections import deque


def D_commend(num):
    return (num * 2) % 10000


def S_commend(num):
    return 9999 if num == 0 else num - 1


def L_R_commend(num):
    a, d = num // 1000, num % 10
    b, c = num // 100 - a * 10, (num % 100 - d) // 10
    lc = b * 1000 + c * 100 + d * 10 + a
    rc = d * 1000 + a * 100 + b * 10 + c
    return lc, rc


def check(cm, alp):
    if not visited[cm]:
        visited[cm] += 1
        case.append([cm, seq + alp])


t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    case = deque([])
    case.append([x, ""])
    visited = [0] * 10001
    visited[x] += 1
    answer = ""

    while True:
        num, seq = case.popleft()
        if num == y:
            answer = seq
            break
        dc, sc = D_commend(num), S_commend(num)
        lc, rc = L_R_commend(num)

        check(dc, "D")
        check(sc, "S")
        check(lc, "L")
        check(rc, "R")

    print(answer)
