def solution(s):
    arr = s.replace('{', '').replace('}', '').split(',')
    nums = list(set(arr))
    cnt = len(nums)
    answer = [0 for _ in range(cnt)]
    for num in nums:
        answer[cnt - arr.count(num)] = int(num)
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
