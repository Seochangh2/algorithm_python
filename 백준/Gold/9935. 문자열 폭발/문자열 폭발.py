target = list(input())

boom = list(input())
result = []
for i in range(len(target)):
    result.append(target[i])
    if result[-1] == boom[-1] and len(result) >= len(boom):
        if result[-len(boom):] == boom:
            for b in boom:
                result.pop()
if result :
    print(''.join(result))
else :
    print("FRULA")