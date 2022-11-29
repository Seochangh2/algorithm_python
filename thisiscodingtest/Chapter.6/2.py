import heapq
N = int(input())
info = []
for n in range(N):
  name , score = input().split()
  heapq.heappush(info,(int(score),name))

names = [y for x,y in info]
print(*names)