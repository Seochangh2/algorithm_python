import heapq
N = int(input())
card = []
for n in range(N):
    heapq.heappush(card,int(input()))
result = 0

while len(card) != 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    sum_num = a+b
    result += sum_num
    heapq.heappush(card,sum_num)
    
print(result)
    