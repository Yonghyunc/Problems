# 백준 문제는... input을..... 그냥 ..... 웅....
import sys
input = sys.stdin.readline


def enq(x):
    global last
    heap.append(x)
    last += 1
    child = last
    parent = last // 2
    while parent and heap[child] > heap[parent]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child, parent = parent, parent // 2


def deq(x):
    global last
    if last == 0:
        print(0)
    else:
        heap[1], heap[last] = heap[last], heap[1]
        print(heap.pop())
        last -= 1
        parent = 1
        child = 2
        while child <= last:
            if child + 1 <= last and heap[child] < heap[child + 1]:
                child += 1
            if heap[parent] < heap[child]:
                heap[parent], heap[child] = heap[child], heap[parent]
                parent, child = child, child * 2
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