# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to
# node n - 1 and return them in any order.
#
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed
# edge from node i to node graph[i][j]).


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        res = []
        s = [[0]]
        while s:
            curr_route = s.pop()
            node = curr_route[-1]
            s += [curr_route + [_] for _ in graph[node]]
            if node == n - 1:
                res.append(curr_route)

        return res


if __name__ == '__main__':
    # graph = [[1, 2], [3], [3], []]
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    res = Solution().allPathsSourceTarget(graph)
    print(res)
