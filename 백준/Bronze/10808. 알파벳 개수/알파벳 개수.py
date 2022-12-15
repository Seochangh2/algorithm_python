import sys
import collections

input = sys.stdin.readline


string = input().rstrip()
result = [0]*26

for s in string:
    result[ord(s)-97] += 1

for r in result:
    print(r,end=" ")