# 시간초과 !!

def sortArr(x):
    for k in range(len(arr)):
        if x <= arr[k]:
            arr.insert(k, x)
            break
    else:
        arr.append(x)


n = int(input())

arr = []
for i in range(n):
    x = int(input())

    if x > 0:
        if len(arr) == 0:
            arr.append(x)
        else:
            sortArr(x)

    else:
        if len(arr) > 0:
            print(arr.pop())
        else:
            print(0)