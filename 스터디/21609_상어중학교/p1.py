from collections import deque


# 중력 함수
def gravity(arr):
    for j in range(n):
        for i in range(n - 1, 0, -1):
            if arr[i][j] == -2:
                k = 1
                while i - k >= 0:
                    if arr[i - k][j] == -1:
                        break
                    elif arr[i - k][j] >= 0:
                        arr[i][j], arr[i - k][j] = arr[i - k][j], arr[i][j]
                        break
                    else:
                        k += 1


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
score = 0
is_possible = True

# 1. 가장 큰 블록 그룹 찾기

while is_possible:
    block_cnt = 0
    rainbow_cnt = 0
    standard = []
    main_group = []
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and 0 < arr[i][j] <= m:
                que = deque([[i, j]])
                block_group = [[i, j]]
                group_num = arr[i][j]
                now_block = 1
                now_rainbow = 0
                visited[i][j] += 2
                while que:
                    x, y = que.popleft()
                    for d in delta:
                        nx, ny = x + d[0], y + d[1]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and (not arr[nx][ny] or arr[nx][ny] == group_num):
                            que.append([nx, ny])
                            block_group.append([nx, ny])
                            visited[nx][ny] += 2
                            now_block += 1
                            if not arr[nx][ny]:
                                now_rainbow += 1
                                visited[nx][ny] -= 1
                for bx, by in block_group:
                    visited[bx][by] -= 1
                if now_block > block_cnt or not standard:
                    block_cnt = now_block
                    main_group = block_group
                    rainbow_cnt = now_rainbow
                    standard = [i, j]
                elif now_block == block_cnt:
                    if now_rainbow > rainbow_cnt:
                        main_group = block_group
                        rainbow_cnt = now_rainbow
                        standard = [i, j]
                    elif now_rainbow == rainbow_cnt:
                        block_cnt = now_block
                        main_group = block_group
                        rainbow_cnt = now_rainbow
                        standard = [i, j]
                    #     if i > standard[0]:
                    #         main_group = block_group
                    #         standard = [i, j]
                    #     elif i == standard[0] and j > standard[1]:
                    #         main_group = block_group
                    #         standard = [i, j]

    if block_cnt < 2:
        is_possible = False
    else:
        # 2. 블록 그룹 제거
        score += block_cnt ** 2
        while main_group:
            x, y = main_group.pop()
            arr[x][y] = -2

        # 3. 중력 적용
        gravity(arr)

        # 4. 격자 반시계 방향 회전
        new_arr = []
        for j in range(n - 1, -1, -1):
            line = []
            for i in range(n):
                line.append(arr[i][j])
            new_arr.append(line)

        # 5. 중력 적용
        gravity(new_arr)
        arr = new_arr

print(score)




