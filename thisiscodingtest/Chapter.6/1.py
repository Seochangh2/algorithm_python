import heapq
N = int(input())
nums = []
for n in range(N):
  heapq.heappush(nums,-int(input()))
result = [-x for x in nums]
print(*result)