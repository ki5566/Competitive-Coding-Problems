# BEGIN ANNOTATION
# PROBLEM URL: https://open.kattis.com/problems/applesack
# TAGS: Greedy, Resource efficiency
# EXPLANATION: We can consider the base case where the number of apples left at some position is k,
# the maximum amount the sack can hold. From this case it is obvious the best option is to move forward k+1 steps,
# using all the apples. Backtracking we can see we want to bring as many apples as possible as far as possible
# before we are left with k apples. We want to be as efficient as possible with moving apples forward.
# This leads to 2 conclusions. First, apples will never travel backwards.
# Second, with each apple consumed to move forward one, we must bring forward as many apples as possible
# This means k-1 apples will pass through for every 1 apple consumed, which is as optimal as possible.
# Repeat until there are equal or less than k apples.
# END ANNOTATION

import math

[n,k] = [int(i) for i in input().split()]

apples = n
distance = 0
while(apples > k):
    apples -= math.ceil(apples/k)
    distance +=1
distance += apples
print(distance + 1)
