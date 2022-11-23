N,M,K = map(int,input().split())



numbers = list(map(int,input().split()))
numbers.sort(reverse=True)

result = 0

max_count = (int(M/(K+1)) * K) + (M%(K+1))

result += max_count*numbers[0]
result += (M-max_count) * numbers[1]

print(result)