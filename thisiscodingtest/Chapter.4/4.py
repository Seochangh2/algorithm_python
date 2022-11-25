N,M = map(int,input().split())
x,y,direct =  map(int,input().split())
start_x , start_y ,x,y= x-1,y-1,x-1,y-1
myMap = []

for n in range(N):
  myMap.append(list(map(int,input().split())))

count = 0 

  
def breakCheck():
  if myMap[x][y-1] < 1 and myMap[x][y+1] < 1 and myMap[x+1][y]<1 and myMap[x-1][y]<1:
    return True
  else :
    return False
  
    

while True:
  if breakCheck :
    if direct == 0 and y+1 < N :
      if myMap[x][y+1] == 0 :
        break
      else:
        y +=1
    elif direct == 1 and x-1 >= 0  :
      if myMap[x-1][y] == 0 :
        break
      else:
        x -=1
    elif direct == 2 and y-1 >= 0  :
      if myMap[x][y-1] == 0 :
        break
      else:
        y -=1  
    elif direct == 3 and x+1 < N  :
      if myMap[x+1][y] == 0 :
        break
      else:
        x +=1  

  if direct == 0:
    if y-1  >= 0 and myMap[x][y-1] >0:
      y -= 1
      count +=1
      if start_x!=x and start_y != y : myMap[x][y] = -1 
    direct = 3
  elif direct == 1:
    if x-1  >= 0 and myMap[x-1][y] >0:
      x -= 1
      count +=1
      if start_x!=x and start_y != y : myMap[x][y] = -1 
    direct = 0
  elif direct == 2:
    if y+1  >= 0 and myMap[x][y+1] >0:
      y += 1
      count +=1
      if start_x!=x and start_y != y : myMap[x][y] = -1 
    direct = 1
  elif direct == 3:
    if x+1  >= 0 and myMap[x+1][y] >0:
      x += 1
      count +=1
      if start_x!=x and start_y != y : myMap[x][y] = -1 
    direct = 2


print(count)