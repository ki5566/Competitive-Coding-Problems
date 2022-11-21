#
# BEGIN ANNOTATION
# PROBLEM URL: https://open.kattis.com/contests/yhycnm/problems/subtractionplusplusplus
# TAGS: dynamic programming
# EXPLANATION: Rather than recursing down every possible subtraction value for each player,
# We can determine for which results which player wins, as this game is solved with predetermined winner.
# Note that the values at which the winner rotates changes by 1 every other turn, and using this
# We can find within which range the number of cobblestone lies in, and thus the winner
# END ANNOTATION

# Read input
num = int(input())
# Declare the first turn as an "Odd" turn
odd = False
# n represents the increment every turn
n = 1
total = 0

# Runs the upper bound of the range is within read input
while(total<num):
    # Increment the total
    total += n
    odd = not odd
    if(odd):
        # Increase the increment every other turn
        n += 1
# Print result
if odd:
    print("YES")
else:
    print("NO")
