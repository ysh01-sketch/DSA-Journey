'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        # code here
        
        if not root or (not root.left and not root.right):
            return True
            
        
        sum = 0
        if  root.left:
            sum += root.left.data
            
        if  root.right:
            sum += root.right.data
            
            
        return (sum == root.data and self.isSumProperty(root.left) and self.isSumProperty(root.right))
            
            
        