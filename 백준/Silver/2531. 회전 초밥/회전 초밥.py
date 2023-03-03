import copy
N,D,K,C = map(int,input().split())
food = []
for n in range(N):
    food.append(int(input()))
food = food + copy.deepcopy(food)
result = -1e9
for n in range(N):
    now = len(set(food[n:n+K]+[C]))
    result = max(result,now)
print(result)