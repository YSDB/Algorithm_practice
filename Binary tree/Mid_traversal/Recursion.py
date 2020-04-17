class TreeNode:
  def __init__(self,x):
    self.val = x
    self.left = None
    self.right = None

lists = []   
def mid_travel(root,lists):
  if not root:
    return
  mid_travel(root.left,lists)
  lists.append(root.val)
  mid_travel(root.right,lists)
  return 
