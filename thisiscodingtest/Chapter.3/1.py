
money = int(input())
coins = [500,100,50,10]
result = 0
for coin in coins:
  result += money // coin
  money %= coin

print(result)
 
