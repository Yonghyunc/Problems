from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001          # 몇 번째에 방문했는지 체크
times = [0] * 100001            # 최선의 시간에 몇 번이나 방문했는지 체크
queue = deque([n])
visited[n] += 1
times[n] += 1

while queue:
    now = queue.popleft()
    if now == k:
        break
    for aft in [now + 1, now - 1, now * 2]:
        # 방문하지 않은 곳이거나, 더 적은 시간에 방문하는 경우 (같은 시간 포함)
        if 0 <= aft <= 100000 and (not visited[aft] or visited[aft] > visited[now]):
            visited[aft] = visited[now] + 1 if visited[aft] != visited[now] else visited[now]
            times[aft] += 1
            queue.append(aft)

print(visited[k] - 1, times[k], sep="\n")