import bisect
N,X = map(int,input().split())
nums = list(map(int,input().split()))

left = bisect.bisect_left(nums,X)
right = bisect.bisect_right(nums,X)
print(right)
print(left)
if right == left :
  print(-1)
else:
  print(right-left)