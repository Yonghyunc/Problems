import sys
input = sys.stdin.readline


n, c = map(int, input().split())
wifi = sorted([int(input()) for _ in range(n)])
start, end = 1, wifi[-1] - wifi[0]


def check(gap):
    installed = 1
    before = wifi[0]
    for i in range(1, n):
        if wifi[i] - before >= gap:
            installed += 1
            before = wifi[i]
    return installed


if c == 2:
    print(wifi[-1] - wifi[0])
else:
    while start <= end:
        mid = (start + end) // 2
        installed_wifi = check(mid)
        if installed_wifi < c:
            end = mid - 1
        else:
            start = mid + 1

    print((start + end) // 2)