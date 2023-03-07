import math

[n,k] = [int(i) for i in input().split()]

apples = n
distance = 0
while(apples > k):
    apples -= math.ceil(apples/k)
    distance +=1
distance += apples
print(distance + 1)