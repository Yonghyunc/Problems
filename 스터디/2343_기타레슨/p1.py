# 이분탐색

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
videos = list(map(int, input().split()))

start, end = max(videos), n * max(videos)
while True:
    mid = (start + end) // 2
    cnt = m - 1
    val = 0
    for v in videos:
        if val + v <= mid:
            val += v
        else:
            val = v
            cnt -= 1
    if cnt >= 0:
        if end == mid:
            print(start)
            break
        end = mid
    elif cnt < 0:
        if start == mid:
            print(end)
            break
        start = mid




