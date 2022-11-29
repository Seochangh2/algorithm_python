array = [5,7,9,0,3,1,6,2,4,8]
leng = len(array)
def quickSort(start,end):
  if start>=end:
    return
  pivot = start
  left = start +1
  right = end
  while left <= right :
    while left<=end and array[pivot] >= array[left]:
      left+=1
    while right > start and array[pivot] <= array[right]:
      right-=1

    if left > right:
      array[pivot] , array[right] = array[right],array[pivot]
    else:
      array[left] , array[right] = array[right],array[left]  
  
  quickSort(start,right-1)
  quickSort(right+1,end)

def pyQiuckSort(ary):
  leng = len(ary)
  if leng <= 1:
    return ary
  pivot = ary[0]

  
  left = [ary[x] for x in range(1,leng) if ary[x]<=pivot]
  right = [ary[x] for x in range(1,leng) if ary[x]>pivot]

  L = pyQiuckSort(left)
  R = pyQiuckSort(right)
  return L+[pivot]+R
#quickSort(0,leng-1)
result = pyQiuckSort(array)
print(result)