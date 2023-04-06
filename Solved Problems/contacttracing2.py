# BEGIN ANNOTATION
# PROBLEM URL: https://open.kattis.com/problems/contacttracing2
# TAGS: Graphs, Dynamic Programming
# EXPLANATION: We note that if a pair comes into contact, each individual in that pair
# that had contacts 2 days earlier and onward did not spread the infection in those contacts.
# Because no infection is spread in those cases, they are essentially pointless and
# we can comb through the input data and remove those cases.
# Now we can iterate from day 1 to the end, and for each day keep track of who is infected
# and who could be infected the next day. Because we do not know who was infected, we assume all people
# who came into contact with those that are already infected received the disease.
# This allows us to keep track of all people who possibly need to be quarantined.
# If we do not comb the data in the beginning and only iterate through,
# we may see a case where a person gets infected twice, which shouldn't be possible,
# and spreads the disease to people whom the disease shouldn't be able to spread to
# END ANNOTATION

# Take input
[n,k,c] = [int(i) for i in input().split()]
cases = [[] for _ in range(k)]
for _ in range(c):
    [a,b,d] = [int(i) for i in input().split()]
    cases[d-1].append((a,b))
    


day_before = set()
to_add_before = set()

# Combs and removes the bad cases
for day_case in reversed(cases):
    day_case[:] = [i for i in day_case if not (i[0] in day_before or i[1] in day_before)]
    day_before.update(to_add_before)
    to_add_before.clear()
    for case in day_case:
        to_add_before.add(case[0])
        to_add_before.add(case[1])

# Converts the cases from pair by day form to adjacency list by day
contacts = [{} for _ in range(k)]
for day,day_cases in enumerate(cases):
    for case in day_cases:
        if case[0] in contacts[day]:
            contacts[day][case[0]].append(case[1])
        else:
            contacts[day][case[0]] = [case[1]]
        if case[1] in contacts[day]:
            contacts[day][case[1]].append(case[0])
        else:
            contacts[day][case[1]] = [case[0]]



infectious = set()
to_be_infectious = set()

# Find possible patient zeros
for i in range(1,n+1):
    infectious.add(i)
to_be_infectious = infectious.difference(day_before)

# Simulate the infection, assuming all people recieving contact are infected
for day in range(0,k):
    infectious = to_be_infectious.copy()
    to_be_infectious.clear()
    for infector in infectious:
        if infector in contacts[day]:
            for person in contacts[day][infector]:
                to_be_infectious.add(person) 

#Print output
sol = []
for i in to_be_infectious:
    sol.append(i)
sol = sorted(sol)
print(len(sol))
for i in sol:
    print(i)

