N = int(input())
result = 0
for n in range(N+1):
  if n == 3 or n == 13 or n == 23:
    result += 60*60
  else :
    result += (15*60)+(45*15)

print(result)