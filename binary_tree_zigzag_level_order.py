# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def zigzagLevelOrder(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
        
    #     ### still struggle with the direction problem 
    #     q1, q2 = [], [] 
    #     out = [] 
    #     if not root: return [] 
    #     q1.append(root) 
    #     level  = 0 
    #     while root or q1:
    #         curr = [] 
    #         size = len(q1)
    #         if level % 2 == 1 : q1 = q1[::-1] 
    #         for i in range(len(q1)):
    #             root = q1.pop(0)
    #             if root !=None :
    #                 curr.append(root.val)
    #                 if level % 2 == 0:
    #                     q2.append(root.left); q2.append(root.right)
    #                 else:
    #                     q2.insert(0, root.right); q2.insert(0,root.left);
    #         if level % 2 == 1 : print "here", ; q2[::] == q2[::-1]
    #         q1[::] = q2;  
    #         q2 = [] 
    #         level += 1 
    #         if curr:
    #             out.append(curr)
    #     return out
                
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        : solution 2
        """
        def bfs(root, level, res):
            if len(res) < level + 1: res.append([])
            if root:
                if level % 2 == 0 : res[level].append(root.val)
                else:res[level].insert(0,root.val)
                bfs(root.left, level + 1, res)
                bfs(root.right, level + 1, res) 
        res = []
        bfs(root, 0, res )
        res = [ x for x in res if x ] 
        return res
            