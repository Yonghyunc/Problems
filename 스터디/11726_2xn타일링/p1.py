# 11726. 2xn 타일링

n = int(input())

if n == 1:
    print(1 % 10007)
else:
    dp = [0] * n
    dp[0], dp[1] = 1, 2

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[n - 1] % 10007)