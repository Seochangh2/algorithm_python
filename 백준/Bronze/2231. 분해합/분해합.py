N = int(input())

for i in range(1,N+1):
    n_sum = sum(map(int,str(i))) + i
    
    if n_sum == N :
        print(i)
        break
    if i == N:
        print(0)
        break

    