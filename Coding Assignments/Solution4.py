# Read the input values as a list of integers
N = [int(i) for i in input(' ').split()]

# Read the input values for N1, N2, N3, N4, N5 as separate lists of integers
N1 = [int(i) for i in input(' ').split()]
N2 = [int(i) for i in input(' ').split()]
N3 = [int(i) for i in input(' ').split()]
N4 = [int(i) for i in input(' ').split()]
N5 = [int(i) for i in input(' ').split()]

# Combine all the separate lists into a single list, N1
N1.extend(N2)
N1.extend(N3)
N1.extend(N4)
N1.extend(N5)

# Sort the list N1 in ascending order
N1.sort()

# Find the elements in N1 that occur more than twice and store them in a set, res
res = set([i for i in N1 if N1.count(i) > 2])

# Print the length of the set res
print(len(res))
