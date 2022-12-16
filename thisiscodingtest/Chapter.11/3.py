S = input()
cnt1 = 0
cnt2 = 0
for s in S.split("0"):
  if "1" in s:
    cnt1 += 1

for s in S.split("1"):
  if "0" in s:
    cnt2 += 1

print(min(cnt1,cnt2))