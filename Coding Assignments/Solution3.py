import sys
input = sys.stdin.readline

# Read the input values from the first line
line1 = list(map(int, input().split(" ")))
k = line1[2]  # Number of dragons to kill
d = line1[3]  # Total number of dragons
list_d = [[0, 0]]  # Initialize a list to store dragon positions

# Read the positions of dragons from subsequent lines and add them to the list
for i in range(d):
    temp_lst = list(map(int, input().split(" ")))
    list_d.append(temp_lst)

# Sort the list of dragon positions based on row number and column number
sort_dlist = sorted(list_d, key=lambda x: (x[0], x[1]))

# Initialize memoization dictionaries
memo_dist = {}
memo_mindist = {}

# Function to calculate the Manhattan distance between two dragons
def distance(j1, j2):
    global memo_dist

    # Check if the distance has already been calculated and stored in the memoization dictionary
    if (f"{j1},{j2}") in memo_dist:
        return memo_dist[(f"{j1},{j2}")]

    # Calculate the Manhattan distance between the dragons
    stepx = abs(sort_dlist[j1][0] - sort_dlist[j2][0])
    stepy = abs(sort_dlist[j1][1] - sort_dlist[j2][1])
    steps = stepx + stepy

    # Store the calculated distance in the memoization dictionary
    memo_dist[(f"{j1},{j2}")] = steps

    return steps

# Function to compute the minimum distance traveled when the ith dragon is killed
def mindist(i, j):
    global memo_dist
    global memo_mindist

    # Base case: When i is 1, the distance is simply the distance between the starting point and the jth dragon
    if i == 1:
        return distance(0, j)

    # If the minimum distance has already been calculated and stored in the memoization dictionary, return it
    if (f"{i},{j}") in memo_mindist:
        return memo_mindist[(f"{i},{j}")]

    # Calculate the minimum distance by considering all possible previous dragons (x) to kill
    dist_list = []
    for x in range(i - 1, j):
        # Check if the distances have already been calculated and stored in the memoization dictionaries
        if (f"{i - 1},{x}") in memo_mindist:
            if (f"{x},{j}") in memo_dist:
                dist_list.append(memo_mindist[(f"{i - 1},{x}")] + memo_dist[(f"{x},{j}")])
            else:
                dist_list.append(memo_mindist[(f"{i - 1},{x}")] + distance(x, j))
        else:
            # If the distances have not been calculated, recursively compute them and store in the dictionaries
            memo_mindist[(f"{i - 1},{x}")] = mindist(i - 1, x)
            if (f"{x},{j}") in memo_dist:
                dist_list.append(memo_mindist[(f"{i - 1},{x}")] + memo_dist[(f"{x},{j}")])
            else:
                dist_list.append(memo_mindist[(f"{i - 1},{x}")] + distance(x, j))

    # Return the minimum distance
    return min(dist_list)

minsteps = []

# Compute the minimum distance traveled for each jth dragon (from the last dragon to the kth dragon)
for j in range(len(sort_dlist) - 1, k - 1, -1):
    minsteps.append(mindist(k, j))

# Print the minimum of all the computed minimum distances
print(min(minsteps))
