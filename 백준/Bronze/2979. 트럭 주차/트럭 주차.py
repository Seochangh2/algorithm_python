import sys
import collections

A,B,C = map(int,input().split())

arrive = []
leave = []
for i in range(3):
    X,Y = map(int,input().split())
    arrive.append( X)
    leave.append(Y)
arrive.sort()
leave.sort()
start = arrive[0]
for i in range(3):
    arrive[i] -= start
    leave[i] -= start

money = 0
for time in range(leave[2]-arrive[0]):
    
    checker = 0
    if time < leave[0] and time >= arrive[0]:
        checker += 1
    if time < leave[1] and time >= arrive[1]:
        checker += 1
    if time < leave[2] and time >= arrive[2]:
        checker += 1
    if checker == 1:
        money += A
    if checker == 2:
        money += 2*B
    if checker == 3:
        money += 3*C

print(money)