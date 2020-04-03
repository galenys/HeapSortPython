import math

def max_heapify(A, i):
    l = 2*i
    r = 2*i + 1
    largest = 0

    if l <= len(A) and A[l-1] > A[i-1]:
        largest = l
    else:
        largest = i
    if r <= len(A) and A[r-1] > A[largest-1]:
        largest = r

    if largest != i:
        A[i-1], A[largest-1] = A[largest-1], A[i-1]
        max_heapify(A, largest)

def build_max_heap(A):
    length = len(A)
    for i in range(math.floor(length/2), 0, -1):
        max_heapify(A,i)

def heap_sort(A):
    build_max_heap(A)
    output = []
    while len(A) > 0:
        A[0], A[-1] = A[-1], A[0]
        output.append(A.pop(-1))
        max_heapify(A, 1)
    return output