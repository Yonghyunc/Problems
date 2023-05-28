# 실패한 방법...


n = int(input())
colors = input()

bc = 0
rc = 0
before = ""
cnt = 1

for i in range(n):
    if i == n - 1:
        if before != colors[i]:
            cnt += 1
    if colors[i] == "B":
        bc += 1
        if before == "R":
            if rc == 1:
                rc = 0
                cnt += 1
        else:
            if rc > 1:
                cnt += 1
        before = "B"

    else:
        rc += 1
        if before == "B":
            if bc == 1:
                bc = 0
                cnt += 1
        else:
            if bc > 1:
                cnt += 1
        before = "R"


print(cnt)