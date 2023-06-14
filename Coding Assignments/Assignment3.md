# Here there be Dragons
*(IOI Training Camp, 2012)*

The kingdom is falling into ruin. People live in fear. Dragons pillage, kill, and just generally cause as much havoc as they possibly can. The king has just sent out a royal decree:

To any man out there who is able to bring me the heads of K dragons, I shall bequeath a lordship–to him, his sons and his grandsons, till the end of time.

Having seen this royal decree, and knowing that you are capable of killing dragons thanks to your extensive medieval combat training, you set out on a quest to hunt down the evil creatures. Being a busy kind of guy, you would like to complete your quest quickly and kill K dragons through the shortest route.

The kingdom is arranged in a grid with R rows, numbered 0 to R-1, and C columns, numbered 0 to C-1. You start your quest at the top left corner of the grid, (0,0).

The total number of dragons in the kingdom is D, of which you have to kill K. Dragons are very territorial in nature, so each row of the grid contains at most one dragon. Also, since the kingdom is situated on a hill, you travel only downwards on the grid, though you may move left or right as you please.

You are told that no two dragons are on the same row of the grid. Also, no dragon is at position (0,0).

For example, suppose the grid has 5 rows and 5 columns with 3 dragons, of which you have to kill any 2. The three dragons are located at (1,4), (2,3) and (4,4), as shown below. In this case, your shortest route is to take 7 steps and kill the dragons in row 1 and row 2. Killing any other combination of 2 dragons takes 8 steps, so this is the minimum possible. Note that once you've killed K dragons, you don't incur any cost to return home. You just want to find how long it takes to do all the killing.

Solution hint:
Number the dragons 1,2,…,D in ascending order of rows. Let mindist(i,j) denote the minimum distance traveled when the jth dragon killed is dragon i. Recall the constraint that there is no dragon at (0,0). Use dynamic programming to compute mindist(i,j) for all values of i and j, then find the minimum among mindist(i,K) for all i ≥ K.

**Input format:**
- Line 1: Four space-separated integers, R, C, K, and D.
- Lines 2 to D+1: Each line has two-space separated integers r and c, the row and column of the corresponding dragon.

**Output format:**
A single integer, the minimum total distance traveled to kill K dragons.
