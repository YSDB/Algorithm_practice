class TreeNode:
  def __init__(self,x):
    self.val = x
    self.left = None
    self.right = None
   
lists = []
def pre_travel(root,lists):
  if not root:
    return
  lists.append(root.val)
  pre_travel(root.left,lists)
  pre_travel(root.right,lists)
  return 
    
