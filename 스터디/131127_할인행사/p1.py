def check(cnt):
    if cnt == [0] * len(cnt):
        return 1
    else:
        return 0


def solution(want, number, discount):
    answer = 0
    cnt = number[::]
    for i, item in enumerate(want):
        cnt[i] -= discount[:10].count(item)
    answer += check(cnt)

    idx = 1
    while idx < len(discount) - 10:
        idx += 1

    for i in range(len(discount) - 10):
        before = want.index(discount[i]) if discount[i] in want else -1
        after = want.index(discount[i + 10]) if discount[i + 10] in want else -1
        if before >= 0:
            cnt[before] += 1
        if after >= 0:
            cnt[after] -= 1
        answer += check(cnt)

    return answer


print(solution(
    ["banana", "apple", "rice", "pork", "pot"],
    [3, 2, 2, 2, 1],
    ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
))

print(solution(
    ["apple"],
    [10],
["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
))