from bisect import bisect_left,bisect_right
def binary_seacrh_recursive(start,end):
  if start > end :
    return -1

  mid = (end+start)//2
  
  if nums[mid] == target:
    return mid
  elif nums[mid] > target:
    result = binary_seacrh_recursive(0,mid-1)
  else:
    result = binary_seacrh_recursive(mid+1,end)

  return result
def binary_search(start,end):

  while start <= end:
    mid = (start+end)//2
    if nums[mid] == target:
      return mid
    elif nums[mid] > target:
      end = mid-1
    else :
      start = mid+1

  return -1

def py_binary_search(target):
  print(bisect_left(nums,target))
  print(bisect_right(nums,target))

N , target = map(int,input().split())

nums = list(map(int,input().split()))

#idx = binary_seacrh_recursive(0,N-1)
idx = binary_search(0,N-1)
print(idx)