# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        return self.dfs(root, ans)
        
        
    def dfs(self, root, ans):
        if root: 
            if root.left:
                self.dfs(root.left, ans)
            ans.append(root.val)
            if root.right:
                self.dfs(root.right, ans)
        else:
            return
        return ans
        