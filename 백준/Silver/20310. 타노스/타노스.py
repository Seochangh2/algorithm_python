S = list(input())

zero = S.count('0')
one = S.count('1')
for i in range(one//2):
    S.remove('1')
S.reverse()

for i in range(zero//2):
    S.remove('0')
S.reverse()
print(''.join(S))