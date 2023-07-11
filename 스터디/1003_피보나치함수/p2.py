t = int(input())

dp = [0, 1]

for _ in range(t):
    n = int(input())
    if len(dp) <= n:
        for i in range(len(dp), n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
    if n > 0:
        print(dp[n - 1], dp[n])
    else:
        print(dp[1], dp[0])