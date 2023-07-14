import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())
arr = [[[] for _ in range(n)] for _ in range(n)]
fireballs = deque([])

for i in range(m):
    r, c, m, s, d = map(int, input().split())
    arr[r - 1][c - 1].append((m, s, d, 0))
    fireballs.append([r - 1, c - 1])

delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


for move in range(k):
    answer = 0
    # 파이어볼 움직이기
    while fireballs:
        x, y = fireballs.popleft()
        while arr[x][y]:
            m, s, d, step = arr[x][y].pop(0)
            if move != step:
                arr[x][y].append((m, s, d, step))
                break
            nx, ny = (x + delta[d][0] * s) % n, (y + delta[d][1] * s) % n
            arr[nx][ny].append((m, s, d, step + 1))

    # 여러 개의 파이어볼 정리
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                # 이동시킨 파이어볼의 새로운 위치 정보 저장
                fireballs.append([i, j])

                # 파이어볼 여러 개라면 합친 후 4등분
                if len(arr[i][j]) >= 2:
                    ball_cnt = len(arr[i][j])
                    m_sum, s_sum = 0, 0
                    di = [0, 0]
                    while arr[i][j]:
                        m, s, d, step = arr[i][j].pop()
                        m_sum += m
                        s_sum += s
                        di[d % 2] += 1
                    new_m = m_sum // 5
                    new_s = s_sum // ball_cnt
                    answer += new_m * 4
                    # 질량이 0이면 그냥 없어짐
                    if new_m:
                        for l in range(4):
                            if not di[0] or not di[1]:
                                arr[i][j].append((new_m, new_s, l * 2, step))
                            else:
                                arr[i][j].append((new_m, new_s, l * 2 + 1, step))
                else:
                    m, s, d, step = arr[i][j][0]
                    answer += m

print(answer)