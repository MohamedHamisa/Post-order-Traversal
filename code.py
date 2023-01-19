class Solution:
   def postorderTraversal(self, root: TreeNode):
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            post_order.append(node.val)
        
        post_order = []
        dfs(root)
        return post_order
