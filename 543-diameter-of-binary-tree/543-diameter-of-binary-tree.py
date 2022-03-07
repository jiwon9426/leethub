# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree2(self, root: Optional[TreeNode]) -> int:
        root.val = 1
        root = self.dfs(root)
        maxL, maxR = 0,0
        if root.left :
            maxL = self.dfs2(root.left, root.left.val) -1
        if root.right:
            maxR = self.dfs2(root.right, root.right.val) -1
        print(root)
        return maxL + maxR
    
    def dfs2(self, root:Optional[TreeNode], maxtmp):
        if root:
            if root.left :
                maxtmp = max(maxtmp, root.left.val)
                self.dfs2(root.left, maxtmp)
            if root.right:
                maxtmp = max(maxtmp, root.right.val)
                self.dfs2(root.right, maxtmp)
        else:
            return 0
        return max(maxtmp, maxtmp)
        
        
    def dfs(self, root:Optional[TreeNode]):
        if root:
            if root.left:
                root.left.val = root.val+1
                self.dfs(root.left)
            if root.right:
                root.right.val = root.val+1
                self.dfs(root.right)
        else :
            return
        return root
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0       # we will make this variable as global using non-local
        def dfs(root):
            nonlocal dia # a non local variable
            
            if not root: # null case
                return 0
            
            lh = dfs(root.left)
            rh = dfs(root.right)
            
            dia = max(dia, lh+rh)  # update the diameter but don't return it
            
            return 1 + max(lh,rh)  # return the depth of subtree
        
        dfs(root)  # calling this fn will update the diameter of the tree
        return dia