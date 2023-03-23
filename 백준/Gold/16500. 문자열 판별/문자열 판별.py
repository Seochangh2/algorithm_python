target = input()
N = int(input())
words = []
for n in range(N):
    words.append(input())
dp=[False]*(len(target)+1)
dp[0] = True
for i in range(len(target)):
    if not dp[i] : 
        continue
    for w in words:
        if target[i:i+len(w)] == w:

            dp[i+len(w)] = True


print(int(dp[len(target)]))