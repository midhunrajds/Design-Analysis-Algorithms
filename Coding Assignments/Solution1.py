from collections import defaultdict

# Step 1: Read inputs for N, M, and K
N, M, K = map(int, input().split())

# Step 2: Create a defaultdict to represent the graph
graph = defaultdict(lambda: [])

# Step 3: Build the graph by adding edges between vertices
for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

# Step 4: Read the list of museums
museums = list(map(int, input().split()))

# Step 5: Initialize variables
visited = [0] * N
list1 = []
counter = 0

# Step 6: Iterate through all vertices
for i in range(N):
    if visited[i] == 0:
        visited[i] = 1
        stack = [i]
        counter = museums[i]
        while len(stack) > 0:
            u = stack.pop()
            for v in graph[u]:
                if visited[v] == 0:
                    counter += museums[v]
                    stack.append(v)
                    visited[v] = 1
        list1.append(counter)

# Step 7: Check if there are enough connected components
if len(list1) < K:
    print(-1)
else:
    # Step 8: Sort the list of sums
    list1.sort()
    counter = 0
    lav = 0
    nik = len(list1) - 1

    # Step 9: Calculate the sum by selecting elements alternatively
    for i in range(K):
        if i % 2 == 0:
            counter += list1[nik]
            nik -= 1
        else:
            counter += list1[lav]
            lav += 1

    # Step 10: Print the final sum
    print(counter)
