# 백준 14620. 꽃길

delta = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
seed = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1), (2, 0), (-2, 0), (0, 2), (0, -2)]


def flower(cost=0, num=0, spots=[]):
    global min_cost

    if cost > min_cost:
        return
    if num == 3:
        if cost < min_cost:
            min_cost = cost
        return

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if not visited[i][j] and prices[i][j] >= 0:
                can = True
                for spot in spots:
                    for d in range(13):
                        if spot[0] + seed[d][0] == i and spot[1] + seed[d][1] == j:
                            can = False
                            break

                if can:
                    spots.append([i, j])
                    visited[i][j] = True
                    flower(cost + prices[i][j], num + 1, spots)
                    spots.pop()
                    visited[i][j] = False


n = int(input())
garden = [list(map(int, input().split())) for _ in range(n)]
prices = [[-1] * n for _ in range(n)]

for i in range(1, n - 1):
    for j in range(1, n - 1):
        for d in range(5):
            prices[i][j] += garden[i + delta[d][0]][j + delta[d][1]]
        prices[i][j] += 1

min_cost = 3001
visited = [[False] * n for _ in range(n)]

flower()
if min_cost == 3001:
    print(0)
else:
    print(min_cost)

