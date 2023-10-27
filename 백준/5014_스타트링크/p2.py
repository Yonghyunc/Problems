'''
백준 5014. 스타트링크

BFS
'''

from collections import deque

floor, start, goal, up, down = map(int, input().split())
visited = [0] * (floor + 1)
bfs = deque([[start, 0]])
min_dep = 1e9
visited[start] += 1

while bfs:
    now, dep = bfs.popleft()
    if goal == now:
        min_dep = min(min_dep, dep)

    if now + up <= floor and not visited[now + up]:
        visited[now + up] += 1
        bfs.append([now + up, dep + 1])

    if now - down > 0 and not visited[now - down]:
        visited[now - down] += 1
        bfs.append(([now - down, dep + 1]))

min_dep = "use the stairs" if min_dep == 1e9 else min_dep
print(min_dep)