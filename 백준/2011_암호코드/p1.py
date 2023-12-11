n = input()
nums = []
for i in n:
    nums.append(i)
dp = [0] * (len(n))
if nums[0] == '0':
    progress, dp[0] = False, 0
else:
    progress, dp[0] = True, 1


if len(n) > 1 and progress:
    if nums[1] == '0':
        if nums[0] + nums[1] <= '26':
            dp[0], dp[1] = 0, 1
        else:
            progress = False
    else:
        if nums[0] + nums[1] <= '26':
            dp[1] = 2
        else:
            dp[1] = 1
    if progress:
        for i in range(2, len(n)):
            if nums[i] == '0':
                if nums[i - 1] > '2':
                    dp[-1] = 0
                    break
                else:
                    dp[i - 1], dp[i] = 0, dp[i - 2]
            else:
                if nums[i - 1] + nums[i] <= '26':
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1]

print(dp[-1] % 1000000)