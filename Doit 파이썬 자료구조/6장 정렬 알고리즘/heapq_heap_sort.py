import heapq
from typing import MutableSequence


def heap_sort(a: MutableSequence) -> None:
    heap = []
    for i in a:
        heapq.heappush(heap, i)
    for i in range(len(a)):
        a[i] = heapq.heappop(heap)