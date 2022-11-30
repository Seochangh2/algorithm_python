import sys

N, M = map(int,input().split())
nums = list(map(int,(sys.stdin.readline().rstrip()).split()))
nums.sort()

def binary_search(start,end):
  max_height = float("-inf")
  m_h_idx = -1
  min_sum = 0
  while start <= end:
    now_sum = 0
    mid = (start+end)//2

    for i in range(mid+1,N):
      now_sum += (nums[i] - nums[mid])

    if now_sum == M:
      return nums[mid]
    elif now_sum > M :
      if max_height < nums[mid]:
        max_height = nums[mid]
        min_sum = now_sum
        m_h_idx = mid

      start = mid+1
    else :
      end = mid-1

  remain = min_sum-M
  larges = (N-1)-m_h_idx

  while remain > 0 :
    count = 0
    if remain == larges:
      count += 1
      return max_height + count
    elif remain > larges:
      count +=1
      remain -= larges
    elif remain < larges:
      return max_height + count
  
def answer(start,end):
  result = 0
  while start<=end:
    total = 0 
    mid = (start+end)//2
    for n in nums:
      if n > mid:
        total += n-mid

    if total >= M :
      result = mid
      start = mid+1
    else :
      end = mid -1
  return result

#result = binary_search(0,N-1)
result = answer(0,nums[-1])
print(result)
