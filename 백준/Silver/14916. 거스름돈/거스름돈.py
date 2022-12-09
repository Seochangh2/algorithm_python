import collections
import sys
sys.setrecursionlimit(10**6)
N = int(input())

memory = collections.defaultdict(int)
memory[2] = 1
memory[5] = 1
def cal(money):
    if money < 2 :
        return sys.maxsize
    
    if money in memory:
        return memory[money]
    min_result = min(cal(money-2),cal(money-5))
    
    memory[money] = min_result + 1
    return memory[money]
cal(N)
if memory[N] >= sys.maxsize or memory[N] == 0 :
    print(-1)
else :
    print(memory[N])
    