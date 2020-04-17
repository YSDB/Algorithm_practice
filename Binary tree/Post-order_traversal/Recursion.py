class TreeNode:
  def __init__(self,x):
    self.val = x
    self.left = None
    self.right = None

lists = []
def pos_travel(root,lists):
  if not root:
    return
  pos_travel(root.left,lists)  
  pos_travel(root.right,lists)
  lists.append(root.val)
  return 
