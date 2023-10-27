'''
백준 5014. 스타트링크

DFS -> 시간 초과
'''

import sys
sys.setrecursionlimit(10**6)

floor, start, goal, up, down = map(int, input().split())
visited = [0] * (floor + 1)
min_dep = 1e9
visited[start] += 1


def dfs(now, dep):
    global min_dep

    if now == goal:
        min_dep = min(min_dep, dep)
        return

    # 위로 가보자
    if now + up <= floor and not visited[now + up]:
        visited[now + up] += 1
        dfs(now + up, dep + 1)
        visited[now + up] -= 1

    # 아래로 가보자
    if now - down > 0 and not visited[now - down]:
        visited[now - down] += 1
        dfs(now - down, dep + 1)
        visited[now - down] -= 1


dfs(start, 0)
min_dep = "use the stairs" if min_dep == 1e9 else min_dep
print(min_dep)