import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
tree = [[] for _ in range(n)]
cut = int(input())
cut_parent = arr[cut]

for i in range(n):
    if arr[i] >= 0 and i != cut:
        tree[arr[i]].append(i)


def delete_child(node):
    for child in tree[node]:
        delete_child(child)
    tree[node] = []


delete_child(cut)


child = []
for i in range(n):
    for j in tree[i]:
        if not len(tree[j]):
            child.append(j)
answer = len(child)

if not answer and cut_parent >= 0:
    print(1)
else:
    print(answer)
