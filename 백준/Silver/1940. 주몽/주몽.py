import sys
input = sys.stdin.readline

N = int(input())
target = int(input())
nums = list(map(int,input().split()))
nums.sort()
cnt = 0
start , end = 0,N-1

while start<end:
    if (nums[start]+nums[end]) == target:
        cnt+=1
        end -= 1
        start += 1
    elif (nums[start]+nums[end]) > target:
        end -= 1
    else :
        start += 1


print(cnt)