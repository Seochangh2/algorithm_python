from collections import defaultdict
memory = defaultdict(int)

def fibo_topdown(x):
  if x<=2 :
    return 1
  
  if x in memory:
    return memory[x]
  
  memory[x] = fibo(x-1)+fibo(x-2)
  return memory[x]

def fibo_bottomup(x):
  memory[1] = 1
  memory[2] = 1

  for num in range(3,x+1):
    memory[num] = memory[num-1]+memory[num-2]
  

