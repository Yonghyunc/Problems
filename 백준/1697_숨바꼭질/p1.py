from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001
location = deque([[n, 0]])
visited[n] += 1
while location:
    now, time = location.popleft()
    if now == k:
        print(time)
        break
    cases = [now + 1, now - 1, now * 2]
    for case in cases:
        if 0 <= case <= 100000 and not visited[case]:
            location.append([case, time + 1])
            visited[case] += 1
