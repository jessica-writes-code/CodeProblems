# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def leafValueSequence(self, root: Optional[TreeNode]) -> List[int]:
        lvs = []

        if root.left is None and root.right is None:
            lvs.append(root.val)
        
        if root.left is not None:
            lvs.extend(self.leafValueSequence(root.left))
        
        if root.right is not None:
            lvs.extend(self.leafValueSequence(root.right))
        
        return lvs

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.leafValueSequence(root1) == self.leafValueSequence(root2)
