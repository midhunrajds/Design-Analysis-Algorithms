# Road Trips and Museums
## Indian National Olympiad in Informatics 2018

Lavanya and Nikhil have K months of holidays ahead of them, and they want to go on exactly K road trips, one a month. They have a map of the various cities in the world with the roads that connect them. There are N cities, numbered from 1 to N. We say that you can reach city B from city A if there is a sequence of roads that starts from city A and ends at city B. Note that the roads are bidirectional. Hence, if you can reach city B from city A, you can also reach city A from city B.

Lavanya first decides which city to start from. In the first month, they will start from that city, and they will visit every city that they can reach by road from that particular city, even if it means that they have to pass through cities that they have already visited previously. Then, at the beginning of the second month, Nikhil picks a city that they haven't visited till then. In the second month, they first fly to that city and visit all the cities that they can reach from that city by road. Then, in the third month, Lavanya identifies a city, and they fly there and visit all cities reachable from there by road. Then in the fourth month, it is Nikhil's turn to choose an unvisited city to start a road trip, and they alternate like this. Note that the city that they fly to (that is, the city from where they start each month's road trip) is also considered as being visited.

Each city has some museums, and when they visit a city for the first time, Lavanya makes them visit each of the museums there. Lavanya loves going to museums, but Nikhil hates them. Lavanya always makes her decisions so that they visit the maximum number of museums possible that month, while Nikhil picks cities so that the number of museums visited that month is minimized.

Given a map of the roads, the number of museums in each city, and the number K, find the total number of museums that they will end up visiting at the end of K months. Print -1 if they will have visited all the cities before the beginning of the Kth month, and hence they will be left bored at home for some of the K months.

## Solution hint
Use BFS/DFS to identify the connected components of the underlying undirected graph. Sort the components based on how many museums they contain and make appropriate choices for Lavanya and Nikhil each month.

## Input format
The first line of each testcase contains three integers: N, M, and K, which represent the number of cities, the number of roads, and the number of months.
The ith of the next M lines contains two integers, ui and vi. This denotes that there is a direct road between city ui and city vi.
The next line contains N integers, the ith of which represents the number of museums in city i.

## Output format
If they can go on K road trips, output a single line containing a single integer which should be the total number of museums they visit in the K months. Output -1 if they can't go on K road trips.

## Constraints
- 1 ≤ N ≤ 106
- 0 ≤ M ≤ 106
- 1 ≤ K ≤ 106
- 1 ≤ ui, vi ≤ N
- There is no road which goes from one city to itself. i.e., ui ≠ vi.
- There is at most one direct road between a pair of cities.
- 0 ≤ Number of museums in each city ≤ 1000
- Sum of N over all testcases in a file will be ≤ 1.5 * 106

[Solution](Solution1.py)
