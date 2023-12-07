n = int(input())
person = list(map(int, input().split()))
line = [0] * n

for i in range(n):
    taller = person[i]
    for j in range(n):
        if not taller and not line[j]:
            line[j] = i + 1
            break
        if not line[j]:
            taller -= 1
print(*line)
