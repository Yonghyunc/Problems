import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())
nutrient = [list(map(int, input().split())) for _ in range(n)]
ground = [[5] * n for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
tree = m
delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


for _ in range(m):
    x, y, age = map(int, input().split())
    trees[x - 1][y - 1].append(age)

five = deque([])

for turn in range(k):
    if not tree:
        break

    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                new_tree = deque([])
                dead = 0
                for t in trees[i][j]:
                    if t <= ground[i][j]:
                        ground[i][j] -= t
                        new_tree.append(t + 1)
                        if (t + 1) % 5 == 0:
                            five.append([i, j])
                    else:
                        dead += t // 2
                        tree -= 1
                trees[i][j] = new_tree
                ground[i][j] += dead

    while five:
        x, y = five.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                tree += 1
                trees[nx][ny].appendleft(1)

    for i in range(n):
        for j in range(n):
            ground[i][j] += nutrient[i][j]


print(tree)
