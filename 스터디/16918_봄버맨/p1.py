height, width, time = map(int, input().split())
grid = [list(input()) for _ in range(height)]


def list_to_string(arr):
    for h in range(len(arr)):
        print(*arr[h], sep="")


def all_bomb(h, w):
    for nh in range(h):
        print('O'*w)


if time % 2 == 0:
    all_bomb(height, width)

else:
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    now_time = 1

    while now_time != time:
        if now_time % 2 != 0:

            #  초기 폭탄 터짐
            for h in range(height):
                for w in range(width):
                    if grid[h][w] == "O":
                        grid[h][w] = "*"
                        for dx, dy in delta:
                            nx, ny = h + dx, w + dy
                            if 0 <= nx < height and 0 <= ny < width:
                                if grid[nx][ny] == ".":
                                    grid[nx][ny] = "*"

            # 재설치
            for h in range(height):
                for w in range(width):
                    if grid[h][w] == "*":
                        grid[h][w] = "."
                    else:
                        grid[h][w] = "O"

        now_time += 1

    list_to_string(grid)

