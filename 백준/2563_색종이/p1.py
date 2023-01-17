# https://www.acmicpc.net/problem/2563

n = int(input())
paper = [[0] * 100 for _ in range(100)]
cnt = 0

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if paper[i][j] == 0:
                paper[i][j] = 1
                cnt += 1
print(cnt)