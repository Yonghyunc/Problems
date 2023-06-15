import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


# 기둥 길이 구하기
def get_pillar(node, dis):
    global pillar_length, giga
    visited[node] += 1
    pillar_length += dis
    giga = node

    if len(tree[node]) > 2:
        return
    else:
        for child, val in tree[node]:
            if not visited[child]:
                get_pillar(child, val)


# 모든 가지 길이 측정
def get_branch(node, dis):
    visited[node] += 1
    distances[node] += dis

    for child, val in tree[node]:
        if not visited[child]:
            distances[child] += distances[node]
            get_branch(child, val)


n, r = map(int, input().split())
tree = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(n - 1):
    a, b, d = map(int, input().split())
    tree[a].append([b, d])
    tree[b].append([a, d])


pillar_length = 0
giga = r
if len(tree[r]) == 1:       # 시작 노드가 기가 노드면 기둥 길이 0
    get_pillar(r, 0)

distances = [0] * (n + 1)
get_branch(giga, 0)

print(pillar_length, max(distances))