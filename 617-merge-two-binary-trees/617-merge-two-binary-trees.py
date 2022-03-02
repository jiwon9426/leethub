class Solution(object):
    def mergeTrees(self, root1, root2):
        
        if not (root1 or root2):
            return None
        root = TreeNode(0)
        stack = [(root, root1,root2)]
        
        while stack:
            node, n1, n2 = stack.pop()

            if n1 and n2:
                node.val = n1.val+n2.val
                if n1.left  or n2.left :
                    node.left = TreeNode(0)
                    stack.append((node.left,n1.left,n2.left))
                if n1.right  or n2.right :
                    node.right = TreeNode(0)
                    stack.append((node.right, n1.right,n2.right))
                    
            elif not n2:
                node.val = n1.val
                if n1.left:
                    node.left = TreeNode(0)
                    stack.append((node.left,n1.left,None))
                if n1.right:
                    node.right = TreeNode(0)
                    stack.append((node.right, n1.right,None))
            
            elif not n1 :
                node.val = n2.val
                if n2.left:
                    node.left = TreeNode(0) 
                    stack.append((node.left,None,n2.left))
                if n2.right:
                    node.right = TreeNode(0)
                    stack.append((node.right, None ,n2.right))
                    
        return root