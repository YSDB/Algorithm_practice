class TreeNode:
  def __init__(self,x):
    self.val = x
    self.left = None
    self.right = None
   
def mid_travel(root):
  if not root:
    return
  mid_travel(root.left)
  root.val
  mid_travel(root.right)
  return 
