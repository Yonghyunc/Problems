from itertools import combinations

n = int(input())
arr = []
teachers = []
nothing = []
for i in range(n):
    line = list(input().split())
    for j in range(n):
        if line[j] == "T":
            teachers.append([i, j])
        if line[j] == "X":
            nothing.append([i, j])
    arr.append(line)
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def watch(x, y):
    watched = True
    for dx, dy in delta:
        nx, ny = x, y
        while 0 <= nx + dx < n and 0 <= ny + dy < n and watched:
            nx += dx
            ny += dy
            if arr[nx][ny] == "S":
                watched = False
            elif arr[nx][ny] == "W":
                break
        if not watched:
            break
    return watched


for case in combinations(nothing, 3):
    for cx, cy in case:
        arr[cx][cy] = "W"
    case_watched = True
    for tx, ty in teachers:
        case_watched = watch(tx, ty)
        if not case_watched:
            break
    for cx, cy in case:
        arr[cx][cy] = "X"
    if case_watched:
        print("YES")
        break
else:
    print("NO")