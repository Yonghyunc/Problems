raw = input()

# 1. 레이저 찾기
laser = [raw[0]]
for i in raw[1:]:
    if i == "(":
        laser.append(i)
    else:
        before = laser.pop()
        if before == "(":
            laser.append('*')
        else:
            laser.append(before)
            laser.append(i)


# 2. 막대 카운트
cnt = laser.count('(')

# 3. 막대 자르기
open_bracket = []
for j in laser:
    if j == "*":
        n = len(open_bracket)
        cnt += n
    elif j == "(":
        open_bracket.append(j)
    else:
        open_bracket.pop()

print(cnt)
