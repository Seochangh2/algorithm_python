import collections

N = int(input())
names = ["CY","SK"]
result = 0
memory = collections.defaultdict(int)
memory[1]=1
memory[2]=2
memory[3]=1

def sol(num):
    if num <= 3:
        return memory[num]
    if num>3:
        if (num) in memory:
            return memory[num]
        else:
            memory[num] = sol(num-3)+1
            return memory[num]
    if num>1:
        if (num) in memory:
            return memory[num]
        else:
            memory[num] = sol(num-1)+1
            return memory[num]

sol(N)
print(names[memory[N]%2])