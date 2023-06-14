# Voting in Siruseri
**(Zonal Computing Olympiad 2010)**

Elections are on for the Siruseri Town Council. Elections in Siruseri work in a rather odd manner. Each candidate is assigned a unique identification number. The town is divided into five zones, and each zone proposes a list of candidates, in some arbitrary order, that it would like to nominate to the Council. Any candidate who is proposed by three or more zones is elected. There is no lower limit or upper limit on the size of the Council.

Your task is to calculate how many candidates are elected to the Council, given the lists proposed by the five zones.

For example, suppose the candidates proposed by the five zones are as follows:

Zone 1: [12, 387, 15, 162, 5]

Zone 2: [14, 162, 92, 387, 7, 748]

Zone 3: [14, 5, 12, 387]

Zone 4: [17, 952, 12, 92, 398, 849]

Zone 5: [14, 5, 92, 12, 387]

In this example, 5 candidates are elected: these are [12, 387, 5, 14, 92].

## Solution hint
Sort each list and then do a 5-way merge.

## Input format
The first line of the input contains five integers N1, N2, N3, N4, and N5, where Nj is the number of candidates proposed by zone j, 1 ≤ j ≤ 5. This is followed by five lines of space-separated integers. For 1 ≤ j ≤ 5, line j+1 of the input has Nj integers representing the list of candidates proposed by zone j.

## Output format
Your output should be a single line consisting of one integer, the total number of candidates elected to the Town Council.
