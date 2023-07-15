from collections import deque

n, m = map(int, input().split())
basket = [list(map(int, input().split())) for _ in range(n)]
delta = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
cross_delta = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
clouds = deque([(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)])
moved_clouds = deque([])
turn = [[0] * n for _ in range(n)]


def water_bug(x, y):
    water = 0
    for d in cross_delta:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < n and 0 <= ny < n and basket[nx][ny]:
            water += 1
    return water


for t in range(1, m + 1):
    d, s = map(int, input().split())
    while clouds:
        x, y = clouds.popleft()
        # 1. 구름 이동
        nx, ny = (x + delta[d][0] * s) % n, (y + delta[d][1] * s) % n
        # 2. 비 내리기
        basket[nx][ny] += 1
        turn[nx][ny] = t
        moved_clouds.append([nx, ny])
    # 3. 물복사버그
    while moved_clouds:
        x, y = moved_clouds.popleft()
        basket[x][y] += water_bug(x, y)

    # 4. 새로운 구름 생성
    for i in range(n):
        for j in range(n):
            if basket[i][j] >= 2 and turn[i][j] != t:
                clouds.append([i, j])
                basket[i][j] -= 2

# 최종 바구니 물 양
water_sum = 0
for i in range(n):
    water_sum += sum(basket[i])
print(water_sum)

