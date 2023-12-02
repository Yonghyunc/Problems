height, width = map(int, input().split())
blocks = list(map(int, input().split()))
answer = 0
highest = max(blocks)
high_idx = []
for i in range(width):
    if blocks[i] == highest:
        high_idx.append(i)
left, right = high_idx[0], high_idx[-1]
answer += highest * (right - left + 1)


def get_blocks(arr):
    global answer
    high = [arr[0], 0]
    for i in range(1, len(arr)):
        if arr[i] > high[0]:
            answer += high[0] * (i - high[1])
            high = [arr[i], i]


get_blocks(blocks[:left + 1])
get_blocks(blocks[right:][::-1])
print(answer - sum(blocks))
