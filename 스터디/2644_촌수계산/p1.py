n = int(input())
parent = [0] * (n + 1)
child = [[] for _ in range(n + 1)]
per1, per2 = map(int, input().split())
m = int(input())
for _ in range(m):
    p, c = map(int, input().split())
    parent[c] = p
    child[p].append(c)

visited = [0] * (n + 1)
answer = 1e9


def find(x, t):
    global answer
    if x == per2:
        answer = min(answer, t)
    if parent[x] and not visited[parent[x]]:
        visited[x] += 1
        find(parent[x], t + 1)
        visited[x] -= 1
    if child[x]:
        for c in child[x]:
            if not visited[c]:
                visited[c] += 1
                find(c, t + 1)
                visited[c] -= 1


find(per1, 0)
if answer == 1e9:
    print(-1)
else:
    print(answer)