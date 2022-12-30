import heapq,sys
def solution(N, stages):
    answer = []
    leng = len(stages)
    for i in range(1,N+1):
        c = stages.count(i)
        if leng > 0:
            heapq.heappush(answer,(-(c/leng),i))
        else :
            heapq.heappush(answer,(0,i))
        leng -= c
    result = []
    while answer:
        v,i = heapq.heappop(answer)
        result.append(i)
    return result