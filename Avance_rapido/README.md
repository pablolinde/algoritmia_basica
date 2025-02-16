"""
The Problem:
We have to write a program that selects the order of execution of the tasks eligible or candidates for execution, as well as the machine on which they should be executed, minimizing the accumulated execution time of the machines. The execution time of each task n on each machine m is known in advance.
Specifically, the goal to minimize is the time at which the machine that finishes last completes its execution (what is known as the accumulated processing time). Any solution whose accumulated processing time is at most triple that of the basic solution devised by the professor will be accepted.

Input:
The first line of the input contains an integer, P, which indicates the number of test cases.
Each test case will start with a line containing two integers, N and M, indicating the number of tasks to execute and the number of available machines, respectively. At most, N and M will be 100.
This is followed by N lines (one per task), each line containing M integers separated by spaces corresponding to the execution time of the task on each of the available machines.
Tasks and machines are numbered starting from 1.

Output:
For each test case, the output should contain three lines. The first line is the accumulated processing time for the machine with the highest load, meaning the time when the last task finishes on the last machine.
The second line must indicate the order in which the tasks are selected. This line will contain N integers, separated by spaces. Each i-th number indicates the task that is executed in the i-th position.
The third line will also contain N integers, indicating on which machine the task selected in the i-th position is executed.

Example Input:
2
5 2
13 25
7 16
22 19
13 14
14 23
7 5
21 22 24 25 9
7 26 22 7 2
21 13 22 17 20
10 19 1 6 12
4 6 10 9 17
13 11 3 19 22
17 13 19 16 13

Example Output:
34
2 4 1 3 5
1 2 1 2 1
16
4 2 5 6 1 3 7
3 5 1 3 5 2 4
"""
