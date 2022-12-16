nums = list(map(int,input()))

nums.sort()
result = 0
if len(nums) == 1:
  print(nums[0])
for i in range(1,len(nums)):
  if nums[i-1] <= 1 :
    result += nums[i]
  else :
    if i == 1:
      result = nums[i]*nums[i-1]
    else:
      result *= nums[i]

print(result)
    