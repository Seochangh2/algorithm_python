N = int(input())
target = list(input())
words = []
result = 0

for _ in range(N-1):
    words.append(list(input()))

result = 0
for word in words:
    compare = target[:]
    cnt = 0
    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1
    if cnt < 2 and len(compare)<2:
        result += 1
print(result)