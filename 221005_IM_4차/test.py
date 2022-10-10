import heapq

N = int(input())
heap = []
for _ in range(N):
    heapq.heappush(heap, list(map(int, input().split())))
    print(heap)
# print(heap)
