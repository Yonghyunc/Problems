# 예전에 푼 풀이

n, k = map(int, input().split())
nums = list(map(int, input().split()))


def temp(nums, k):
    max_sum = -100 * k
    start = 0
    curr_sum = 0

    for end, val in enumerate(nums):
        curr_sum += val
        if end - start + 1 == k:
            max_sum = max(max_sum, curr_sum)
            curr_sum -= nums[start]
            start += 1
    return max_sum


print(temp(nums, k))