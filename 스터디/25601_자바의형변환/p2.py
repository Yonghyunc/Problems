n = int(input())
tree = {}
for _ in range(n - 1):
    a, b = input().split()
    tree[a] = b             # 자식은 오직 하나의 부모를 가짐


def find_relation(child, target):
    node = child
    while tree.get(node):
        node = tree[node]
        if node == target:
            return True


a, b = input().split()
print(int(find_relation(a, b) or find_relation(b, a) or 0))