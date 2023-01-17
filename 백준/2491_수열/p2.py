n = int(input())
nums = list(map(int, input().split()))

max_len = 0
status = 0      # max = 1 / min = 2
length = 1

if len(nums) == 1:
    max_len = 1
else:
    for i in range(n - 1):
        if status == 0:
            length += 1
            if nums[i] > nums[i + 1]:
                status = 2
            elif nums[i] < nums[i + 1]:
                status = 1

        elif status == 1:
            if nums[i] <= nums[i + 1]:
                length += 1
            else:
                status = 2
                if length > max_len:
                    max_len = length

        elif status == 2:
            if nums[i] >= nums[i + 1]:
                length += 1
            else:
                status = 1
                if length > max_len:
                    max_len = length

        print(nums[i], nums[i + 1], length, status)
        if i == n - 2:
            if length > max_len:
                max_len = length

print(max_len)