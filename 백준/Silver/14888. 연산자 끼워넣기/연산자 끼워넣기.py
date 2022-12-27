import itertools,sys
N = int(input())
nums = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())

max_result = -sys.maxsize
min_result = sys.maxsize

def sol(i,result):
    global add,sub,mul,div,max_result,min_result
    if i == N:
        max_result = max(max_result,result)
        min_result = min(min_result,result)
    if add > 0:
        add -= 1
        sol(i+1,result + nums[i])
        add += 1
    if sub > 0:
        sub -=1
        sol(i+1,result - nums[i])
        sub +=1
    if mul >0:
        mul -=1
        sol(i+1,result*nums[i])
        mul +=1
    if div >0:
        div -=1
        sol(i+1,int(result/nums[i]))
        div +=1
sol(1,nums[0])
print(max_result)
print(min_result)