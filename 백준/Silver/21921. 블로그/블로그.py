import sys
import collections

input = sys.stdin.readline

N,X  =  map(int,input().split())
nums = list(map(int,input().split()))
counter = collections.defaultdict(int)

start , end = 0,X-1

now_sum = sum(nums[:X]) - nums[end] 
max_sum = -sys.maxsize
while end < N :
    now_sum = now_sum + nums[end] 
    counter[now_sum] += 1
    max_sum = max(max_sum,now_sum)
    now_sum -= nums[start]
    end += 1
    start += 1
if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(counter[max_sum])