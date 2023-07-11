import sys
input = sys.stdin.readline

n, m = map(int, input().split())
office = []
cameras = []
blank = 0
for i in range(n):
    line = list(map(int, input().split()))
    office.append(line)
    for j in range(m):
        # 카메라 위치 저장
        if 1 <= line[j] <= 5:
            cameras.append([i, j])
        # 초기 빈칸 수 파악
        elif not line[j]:
            blank += 1


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
camera_1 = [[0], [1], [2], [3]]
camera_2 = [[0, 2], [1, 3]]
camera_3 = [[0, 1], [1, 2], [2, 3], [3, 0]]
camera_4 = [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]
camera_5 = [[0, 1, 2, 3]]


# cctv 하나의 감시 영역 체크
def delta_move(x, y, c, idx):
    global blank
    for d in c:
        nx, ny = x, y
        while True:
            nx, ny = nx + delta[d][0], ny + delta[d][1]
            if 0 <= nx < n and 0 <= ny < m:
                if not office[nx][ny]:
                    blank -= 1
                    office[nx][ny] = idx
                elif office[nx][ny] == 6:
                    break
            else:
                break


# cctv 하나의 감시 영역 해제
def delta_remove(x, y, c, idx):
    global blank
    for d in c:
        nx, ny = x, y
        while True:
            nx, ny = nx + delta[d][0], ny + delta[d][1]
            if 0 <= nx < n and 0 <= ny < m:
                if office[nx][ny] == idx:
                    blank += 1
                    office[nx][ny] = 0
                elif not office[nx][ny]:
                    break
            else:
                break


# cctv 번호
def choose_camera(x, y):
    if office[x][y] == 1:
        return camera_1
    elif office[x][y] == 2:
        return camera_2
    elif office[x][y] == 3:
        return camera_3
    elif office[x][y] == 4:
        return camera_4
    elif office[x][y] == 5:
        return camera_5


# dfs를 위한 재귀 함수 (1 ~ 4번 cctv는 가질 수 있는 방향의 경우의 수가 여러 개)
# idx (cctv 번호) 를 설정해 준 이유 => 감시 영역 해제 시 혼동 막기 위해
def view(x, y, idx=7):
    global min_blank
    for c in choose_camera(x, y):
        delta_move(x, y, c, idx)
        if cameras:
            nx, ny = cameras.pop()
            view(nx, ny, idx + 1)
            delta_remove(x, y, c, idx)
        else:
            min_blank = min(min_blank, blank)
            delta_remove(x, y, c, idx)
    cameras.append([x, y])


min_blank = blank
# cctv가 없는 경우도 있을 수 있음
if cameras:
    x, y = cameras.pop()
    view(x, y)
print(min_blank)