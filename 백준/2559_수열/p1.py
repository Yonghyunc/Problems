# https://www.acmicpc.net/problem/2559

n, k = map(int, input().split())
nums = list(map(int, input().split()))

days = nums[:k]
temp = sum(days)

max_temp = temp

for i in range(k, n):
    front = days.pop(0)
    temp -= front
    days.append(nums[i])
    temp += nums[i]

    if temp > max_temp:
        max_temp = temp

print(max_temp)