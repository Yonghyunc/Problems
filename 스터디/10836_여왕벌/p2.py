# python => 83점
# pypy => 100점

m, n = map(int, input().split())
honeycomb = [1] * (2 * m - 1)

for _ in range(n):
    a, b, c = map(int, input().split())
    idx = 0
    while a:
        a -= 1
        idx += 1
    while b:
        honeycomb[idx] += 1
        b -= 1
        idx += 1
    while c:
        honeycomb[idx] += 2
        c -= 1
        idx += 1


print(*honeycomb[m - 1:])
for i in range(m - 2, -1, -1):
    print(honeycomb[i], *honeycomb[m:])
