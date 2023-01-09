# You are given nth tasks labeled from 0 to n - 1 represented by a 2D integer array tasks,
# where tasks[i] = [enqueueTimei, processingTimei] means that the ith task will be available to process at
# enqueueTimei and will take processingTimei to finish processing.
#
# You have a single-threaded CPU that can process at most one task at a time and will act in the following way:
#
# If the CPU is idle and there are no available tasks to process, the CPU remains idle.
# If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time.
# If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
# Once a task is started, the CPU will process the entire task without stopping.
# The CPU can finish a task then start a new one instantly.
# Return the order in which the CPU will process the tasks.

from heapq import *


class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """

        qtime_hp = []
        ptime_hp = []
        for i in range(len(tasks)):
            heappush(qtime_hp, (tasks[i][0], tasks[i][1], i))

        curr_time = qtime_hp[0][0]
        res = []
        while len(qtime_hp) > 0:
            task = heappop(qtime_hp)
            if task[0] <= curr_time:
                heappush(ptime_hp, (task[1], task[2]))
            else:
                if len(ptime_hp) > 0:
                    pro_task = heappop(ptime_hp)
                    res.append(pro_task[1])
                    curr_time += pro_task[0]
                    heappush(qtime_hp, task)
                else:
                    curr_time = task[0]
                    heappush(ptime_hp, (task[1], task[2]))

        while len(ptime_hp) > 0:
            res.append(heappop(ptime_hp)[1])

        return res


if __name__ == '__main__':
    tasks = [[1, 2], [2, 4], [3, 2], [4, 1], [22, 6], [22, 1]]
    res = Solution().getOrder(tasks)

    print(res)
