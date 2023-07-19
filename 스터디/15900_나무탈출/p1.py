import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0] * (n + 1)
time = 0
que = deque([[1, 0]])
visited[1] += 1
while que:
    p, t = que.popleft()
    is_leaf = True
    for c in tree[p]:
        if not visited[c]:
            que.append([c, t + 1])
            visited[c] += 1
            is_leaf = False
    if is_leaf:
        time += t

if time % 2:
    print('Yes')
else:
    print('No')