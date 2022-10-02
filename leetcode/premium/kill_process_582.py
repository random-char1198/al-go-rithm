# You have n processes forming a rooted tree structure. You are given two integer arrays pid and ppid, where pid[i] is the ID of the ith process and ppid[i] is the ID of the ith process's parent process.
#
# Each process has only one parent process but may have multiple children processes. Only one process has ppid[i] = 0, which means this process has no parent process (the root of the tree).
#
# When a process is killed, all of its children processes will also be killed.
#
# Given an integer kill representing the ID of a process you want to kill, return a list of the IDs of the processes that will be killed. You may return the answer in any order.

# Input: pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
# Output: [5,10]
# Explanation: The processes colored in red are the processes that should be killed.
#
#
# Input: pid = [1], ppid = [0], kill = 1
# Output: [1]

from collections import defaultdict


class Solution:
    def __init__(self):
        self.res = []
        self.dic = defaultdict(list)

    def dfs(self, kill_num):
        self.res.append(kill_num)
        for child in self.dic[kill_num]:
            self.dfs(child)

    def killProcess(self, pid: list[int], ppid: list[int], kill: int) -> list[int]:
        for i in range(len(pid)):
            # print(ppid[i], pid[i])
            self.dic[ppid[i]].append(pid[i])
        print(self.dic)
        self.dfs(kill_num=kill)


s = Solution()
s.killProcess([1, 3, 10, 5], [3, 0, 5, 3], 5)
