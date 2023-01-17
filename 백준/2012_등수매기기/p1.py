# https://www.acmicpc.net/problem/2012

n = int(input())
fore = []
for _ in range(n):
    fore.append(int(input()))

fore.sort()

diff = 0
for i in range(n):
    diff += abs(i + 1 - fore[i])

print(diff)