N = int(input())
pills = []
for n in range(N):
    l,h = map(int,input().split())
    pills.append((l,h))
max_L = 0
max_H = 0
max_I = 0
for n in range(N):
    if pills[n][1] > max_H:
        max_H,max_I = pills[n][1],pills[n][0]
    if pills[n][0] > max_L:
        max_L = pills[n][0]
box = [0]*(max_L+1)
for l,h in pills:
    box[l] = h
result = 0
h = 0
for i in range(max_I+1):
    if box[i] > h:
        h = box[i]
    result += h
h=0
for i in range(max_L,max_I,-1):
    if box[i] > h:
        h = box[i]
    result += h

print(result)