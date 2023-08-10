import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
blue, white = 0, 0

queue = deque([])
queue.append([0, 0, n - 1, n - 1])


def check_paper(x1, y1, x2, y2):
    global blue, white
    b = 0
    for i in range(x1, x2 + 1):
        b += arr[i][y1:y2 + 1].count(1)

    if 0 < b < (x2 - x1 + 1) * (y2 - y1 + 1):
        return False
    else:
        if b == 0:
            white += 1
        else:
            blue += 1
        return True


while queue:
    x1, y1, x2, y2 = queue.popleft()
    av = check_paper(x1, y1, x2, y2)

    # 종이 4등분
    if not av:
        xc, yc = x1 + (x2 - x1) // 2, y1 + (y2 - y1) // 2
        queue.append([x1, y1, xc, yc])
        queue.append([x1, yc + 1, xc, y2])
        queue.append([xc + 1, y1, x2, yc])
        queue.append([xc + 1, yc + 1, x2, y2])

print(white, blue, sep="\n")