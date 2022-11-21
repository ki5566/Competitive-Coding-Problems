#
# BEGIN ANNOTATION
# PROBLEM URL: https://open.kattis.com/problems/fibtour
# TAGS: fibonacci, dynamic programming
# EXPLANATION: We pre-initialize a dictionary of fibonacci numbers to allow for quick checking of the current and next term.
# We read the heights of the buildings and store them,
# then store the connections as a graph. Using the pre-built dictionary, we can check whether the connection is valid or not
# and draw a directional connection between the two nodes. Then we recurse through each node, taking the length of that node
# to be the max of the node it points to +1. We can reduce the time complexity by memoizing the length of nodes, so we don't
# have to recalculate nodes. To account for loops with the 1,1 start of fibonacci, we ignore that link and assign nodes that
# have a 1,1 connection to them +1 for final values.
# END ANNOTATION

#Read n and m
[n,m] = [int(i) for i in input().split()]

#Read the heights of the buildings
nums = [int(i) for i in input().split()]

#For numsTo[i], holds the nodes that i can reach
numsTo = []
for _ in range(n):
    numsTo.append([])

#Holds if the position has a 1,1 connection
hasStarter = [False]*n

#Fibonacci dictionary
next_fib = {}
a,b=1,2
# At term 100, value is above problem limit of 10^18
for _ in range(100):
    #Assign values to dictionary
    next_fib[a]=b
    a,b=b,a+b

# Stores already calculated values in memory
global memory
memory = [-1]*n

# Read connection input
for _ in range(m):
    [a,b] = [(int(i)-1) for i in input().split()]
    
    #Check if numbers are fibonacci
    if nums[a] not in next_fib or nums[b] not in next_fib:
        continue
    
    #Check for 1,1 edge case
    if nums[a] == 1 and nums[b] == 1:
        hasStarter[a]=True
        hasStarter[b]=True
        continue
    
    # Make building at 'a' be less than 'b' to create directed graph
    if(nums[a]>nums[b]):
        a,b=b,a
    
    # Creates connection if the two are in sequence
    if next_fib[nums[a]] == nums[b]:
        numsTo[a].append(b)

# Recursive function
def recur(num, numsTo):
    
    # Base case, if child nodes length is 1
    if len(numsTo[num]) == 0:
        memory[num]=1
        return 1
        
    # Sets value to 1+ the max of the child nodes, checking for memoization
    val = 1 + max([memory[i] if memory[i] != -1 else recur(i,numsTo) for i in numsTo[num]])
    
    # Assigns value to memory and returns up
    memory[num]=val
    return val

# Base length is 0 for no path
sol=[0]*n
# Calculate the longest path for each node
for i in range(n):
    # Only "start" path if height is in fibonacci sequence
    if nums[i] in next_fib:
        sol[i]=recur(i,numsTo)+int(hasStarter[i])

# Print longest path
print(max(sol))
