'''
백준 16235. 나무 재테크

시간초과
'''


import sys
input = sys.stdin.readline
from collections import deque


n, m, k = map(int, input().split())
nutrient = [list(map(int, input().split())) for _ in range(n)]
ground = [[5] * n for _ in range(n)]
trees = [[0] * n for _ in range(n)]
tree = m
delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

for _ in range(m):
    x, y, age = map(int, input().split())
    trees[x - 1][y - 1] = [age]
dead = deque([])
five = deque([])


for turn in range(k):
    if not tree:
        break

    # 봄
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                trees[i][j].sort()
                new_tree = []
                for t in trees[i][j]:
                    if t <= ground[i][j]:
                        ground[i][j] -= t
                        new_tree.append(t + 1)
                        if (t + 1) % 5 == 0:
                            five.append([i, j])
                    else:
                        dead.append([i, j, t])
                        tree -= 1
                trees[i][j] = new_tree

    # 여름
    while dead:
        i, j, t = dead.popleft()
        ground[i][j] += t // 2

    # 가을
    while five:
        i, j = five.popleft()
        for dx, dy in delta:
            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < n:
                tree += 1
                if trees[nx][ny]:
                    trees[nx][ny].append(1)
                else:
                    trees[nx][ny] = [1]

    # 겨울
    for i in range(n):
        for j in range(n):
            ground[i][j] += nutrient[i][j]


print(tree)



# for turn in range(k):
#     if not tree:
#         break
#
#     # 봄
#     for i in range(n):
#         for j in range(n):
#             if trees[i][j]:
#                 trees[i][j].sort()
#                 new_tree = []
#                 for t in trees[i][j]:
#                     if t <= ground[i][j]:
#                         ground[i][j] -= t
#                         new_tree.append(t + 1)
#                     else:
#                         dead.append([i, j, t])
#                         tree -= 1
#                 trees[i][j] = new_tree
#
#     # 여름
#     while dead:
#         i, j, t = dead.popleft()
#         ground[i][j] += t // 2
#
#     # 가을
#     for i in range(n):
#         for j in range(n):
#             if trees[i][j]:
#                 for t in trees[i][j]:
#                     if t % 5 == 0:
#                         for dx, dy in delta:
#                             nx, ny = i + dx, j + dy
#                             if 0 <= nx < n and 0 <= ny < n:
#                                 tree += 1
#                                 if trees[nx][ny]:
#                                     trees[nx][ny].append(1)
#                                 else:
#                                     trees[nx][ny] = [1]
#
#     # 겨울
#     for i in range(n):
#         for j in range(n):
#             ground[i][j] += nutrient[i][j]
#
# print(tree)