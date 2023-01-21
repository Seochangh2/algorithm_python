def sol(left,right,nums):
  if left>right :
    return None
  
  mid = (left+right)//2
  if nums[mid] == mid:
    return mid
  elif nums[mid] < mid:
    if nums[right] < mid:
      return None
    else:
      return sol(mid+1,right,nums)
  elif nums[mid] > mid:
    if nums[left] > mid:
      return None
    else:
      return sol(left,mid-1,nums)

N = int(input())
nums = list(map(int,input().split()))
result = sol(0,N-1,nums)
if result:
  print(result)
else:
  print(-1)