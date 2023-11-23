import sys
input = sys.stdin.readline

n = int(input())
balls = []
max_color = 0
for i in range(n):
    color, num = map(int, input().split())
    max_color = max(max_color, color)
    balls.append([color, num, i])

result = [0] * n
colors = [0] * (max_color + 1)

balls.sort(key=lambda x: x[1])
accumulate_balls = [0] * n
colors[balls[0][0]] = balls[0][1]

last = 0
rest = []

for i in range(1, n):
    color, num, idx = balls[i]
    if balls[i - 1][1] == num:
        accumulate_balls[i] = accumulate_balls[i - 1]
        if not rest:
            rest.append(balls[i - 1][0])
        rest.append(color)
    else:
        accumulate_balls[i] = accumulate_balls[i - 1] + balls[i - 1][1]
        if rest:
            accumulate_balls[i] += last * (len(rest) - 1)
            rest = []
    same = rest.count(color) - 1
    result[idx] = accumulate_balls[i] - colors[color]
    if same > 0:
        result[idx] += num * same
    colors[color] += num
    last = num

print(*result, sep="\n")