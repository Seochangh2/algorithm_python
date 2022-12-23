N = input()
half = (len(N)//2) 

a1 = list(map(int,N[:half]))
a2 = list(map(int,N[half:]))
if sum(a1) == sum(a2):
  print("LUCKY")
else:
  print("READY")
