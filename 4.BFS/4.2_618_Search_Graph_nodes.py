"""
Description
__________
Given a undirected graph, a node and a target, return the nearest node to given node which value of it is target, return NULL if you can't find.

There is a mapping store the nodes' values in the given parameters.

 Notice

It's guaranteed there is only one available solution

Have you met this question in a real interview? Yes
Example
2------3  5
 \     |  |
  \    |  |
   \   |  |
    \  |  |
      1 --4
Give a node 1, target is 50

there a hash named values which is [3,4,10,50,50], represent:
Value of node 1 is 3
Value of node 2 is 4
Value of node 3 is 10
Value of node 4 is 50
Value of node 5 is 50

Return node 4

Approach
________________________
Standard BFS. remember things that enter queue should be marked as visited,
not when it's popped

Complexity
_______________

TIme - O(N)
Complexity - O(N)
"""

# Definition for a undirected graph node


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {UndirectedGraphNode[]} graph a list of undirected graph node
    # @param {dict} values a dict, <UndirectedGraphNode, (int)value>
    # @param {UndirectedGraphNode} node an Undirected graph node
    # @param {int} target an integer
    # @return {UndirectedGraphNode} a node

    def searchNode(self, graph, values, node, target):
        # Write your code here
        if node is None or target is None or graph is None:
            return
        if len(graph) == 0:
            return

        from collections import deque
        q = deque()
        q.append(node)
        visited = set([node])
 
        while q:
            cur = q.popleft()
            if values[cur] == target:
                return cur
            for neighbor in cur.neighbors:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
        return None
