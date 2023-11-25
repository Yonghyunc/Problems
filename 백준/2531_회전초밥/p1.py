import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
max_plate = 0

for s in range(n):
    end = 0 if s + k < n else s + k - n
    case = sushi[s: s + k] + sushi[: end]
    plate = 0 if c in case else 1
    plate += len(set(case))
    max_plate = max(max_plate, plate)
print(max_plate)