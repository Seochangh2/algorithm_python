import sys
input = sys.stdin.readline
N = int(input())
ctr = list(map(int,input().split()))
money = int(input())
ctr.sort()
ctr_sum = sum(ctr)
if ctr_sum <= money:
    print(ctr[N-1])
else:
    start ,end = 0,ctr[N-1]
    result = 0
    while start<=end:
        mid = (start+end) // 2
        check = 0
        for c in ctr:
            if mid < c:
                check+=mid
            else :
                check+=c
        if check <= money:
            result = mid
            start = mid+1
        else :
            end = mid-1
    print(result)
    