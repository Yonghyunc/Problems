# 시간 초과

def enq(x):
    heap.append(x)
    idx = len(heap) - 1
    while idx > 0 and idx // 2 >= 0 and heap[idx] > heap[idx // 2]:
        heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
        idx //= 2


def deq(x):
    last_idx = len(heap) - 1
    if last_idx == 0:
        print(0)
    else:
        heap[0], heap[last_idx] = heap[last_idx], heap[0]
        print(heap.pop())
        now_idx = 0
        while now_idx * 2 < last_idx:
            kid_idx = now_idx * 2
            if kid_idx + 1 < last_idx and heap[kid_idx] < heap[kid_idx + 1]:
                kid_idx += 1
            if heap[now_idx] < heap[kid_idx]:
                heap[now_idx], heap[kid_idx] = heap[kid_idx], heap[now_idx]
                now_idx = kid_idx
            else:
                break


n = int(input())

heap = [-1]
last = 0
for i in range(n):
    x = int(input())
    if x > 0:
        enq(x)
    else:
        deq(x)
    # print("heap", heap)



