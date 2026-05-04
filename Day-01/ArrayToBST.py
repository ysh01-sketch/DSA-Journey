'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def sortedArrayToBST(self, arr):
        # code here
        
    
        
        end = len(arr)-1
     
        
        def convert(left,right):
            
            if left>right:
                return None
                
            
       
        
            mid = (right+left)//2
            
            
            
            
            root = Node(arr[mid])
            
            root.left = convert(left,mid-1)
            root.right = convert(mid+1,right)
            
            return root
        
        return convert(0, end)
    
    
    
    
    
    
            
            