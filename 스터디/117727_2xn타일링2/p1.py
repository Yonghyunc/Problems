# 백준 11727. 2×n 타일링 2

n = int(input())

dp = [0, 1]

for i in range(1, n):
    if i % 2 == 0:
        dp.append(dp[i] * 2 - 1)
    else:
        dp.append((dp[i] * 2 + 1))

print(dp[-1] % 10007)