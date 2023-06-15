# 틀린 코드!!!!!

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


n, r = map(int, input().split())
tree = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)


def dfs(node, dis):
    visited[node] += 1
    distances[node] += dis

    for child, val in tree[node]:
        if not visited[child]:
            distances[child] += distances[node]
            dfs(child, val)


# 루트노드 밖에 없는 경우
if n == 1:
    print(0, 0)

else:
    for i in range(n - 1):
        a, b, d = map(int, input().split())
        tree[a].append([b, d])
        tree[b].append([a, d])

    # 기둥 길이 측정 - bar_length
    parent = tree[r]

    bar_length = 0
    visited[r] += 1
    breaker = False
    # 시작 노드가 기가 노드가 아닌 경우만
    if len(parent) == 1:
        while not breaker and len(parent) <= 2:
            for child, length in parent:
                if not visited[child]:
                    bar_length += length
                    visited[child] += 1
                    parent = tree[child]
                    breaker = False
                else:
                    breaker = True

    distances = [0] * (n + 1)
    # 모든 가지 길이 측정
    for node, dis in parent:
        if not visited[node]:
            dfs(node, dis)
    print(distances)
    print(bar_length, max(distances))