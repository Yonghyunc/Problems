# https://www.acmicpc.net/problem/2491

n = int(input())
nums = list(map(int, input().split()))

max_len = 0
status = 0      # max = 1 / min = 2

if len(nums) == 1:
    max_len = 1
else:
    length = 1
    for i in range(1, n):

        if nums[i - 1] < nums[i]:       # 점점 커짐
            if status == 2:
                if max_len < length:
                    max_len = length
                length = 2
            else:
                length += 1
            status = 1

        elif nums[i - 1] > nums[i]:    # 점점 작아짐
            if status == 1:
                if max_len < length:
                    max_len = length
                length = 2
            else:
                length += 1
            status = 2

        else:
            length += 1

        if i == n - 1:
            if max_len < length:
                max_len = length

print(max_len)

