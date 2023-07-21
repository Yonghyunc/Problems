k = int(input())
nums = list(map(int, input().split()))
now_length = len(nums)
depth = 0

while depth < k:
    arr_len = now_length // 2 ** depth
    start = 0
    center = arr_len // 2
    while start <= now_length:
        end = start + arr_len
        print(nums[start + center], end=" ")
        start = end + 1
    depth += 1
    print(end="\n")