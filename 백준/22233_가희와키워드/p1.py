import sys
input = sys.stdin.readline

n, m = map(int, input().split())
keywords = {}
for _ in range(n):
    keywords[input().strip()] = 0
memo = n

for _ in range(m):
    for u in input().strip().split(','):
        if u in keywords:
            if not keywords.get(u):
                memo -= 1
            keywords[u] += 1
    print(memo)