import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ver = [[(0, 0), (1, 0)], [(0, 1), (1, 1)], [(1, 0), (2, 0)], [(1, 1), (2, 1)],
       [(0, 0), (2, 0)], [(0, 1), (2, 1)], [(0, 1), (2, 0)], [(0, 0), (2, 1)]]
hor = [[(0, 0), (0, 1)], [(0, 1), (0, 2)], [(1, 0), (1, 1)], [(1, 1), (1, 2)],
       [(0, 0), (1, 2)], [(1, 0), (0, 2)], [(0, 0), (0, 2)], [(1, 0), (1, 2)]]


def vertical_bar(i, j):
    val = 0
    if i + 3 < n:
        for k in range(4):
            val += arr[i + k][j]
    return val


def horizon_bar(i, j):
    val = 0
    if j + 3 < m:
        val += sum(arr[i][j:j + 4])
    return val


def square(i, j):
    val = 0
    if i + 1 < n and j + 1 < m:
        for k in range(2):
            val += sum(arr[i + k][j:j + 2])
    return val


def vertical_rectangle(i, j):
    whole = 0
    if i + 2 < n and j + 1 < m:
        for k in range(3):
            whole += sum(arr[i + k][j:j + 2])
        min_minus = whole
        for v_case in ver:
            val = 0
            for v in v_case:
                val += arr[i + v[0]][j + v[1]]
            min_minus = min(min_minus, val)
        return whole - min_minus
    return whole


def horizon_rectangle(i, j):
    whole = 0
    if i + 1 < n and j + 2 < m:
        for k in range(2):
            whole += sum(arr[i + k][j:j + 3])
        min_minus = whole
        for h_case in hor:
            val = 0
            for h in h_case:
                val += arr[i + h[0]][j + h[1]]
            min_minus = min(min_minus, val)
        return whole - min_minus
    return whole


answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer, max(vertical_bar(i, j), horizon_bar(i, j),
                                 square(i, j), vertical_rectangle(i, j),
                                 horizon_rectangle(i, j)))
print(answer)
