import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, start, end = map(int, input().split())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, v = map(int, input().split())
    tree[a].append([b, v])
    tree[b].append([a, v])

visited = [0] * (n + 1)
min_path = 1e9
nodes = []


def goTo(node, val=0):
    global min_path
    if node == end:
        min_path = min(min_path, val - max(nodes))

    for n, v in tree[node]:
        if not visited[n]:
            visited[n] += 1
            nodes.append(v)
            goTo(n, val + v)
            nodes.pop()
            visited[n] -= 1


if start != end:
    goTo(start)
else:
    min_path = 0
print(min_path)
