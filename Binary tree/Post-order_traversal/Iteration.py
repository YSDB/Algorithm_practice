class TreeNode:
  def __init__(self,x):
    self.val = x
    self.left = None
    self.right = None
    
stack = [root]
lists = []
while stack:
  root = stack.pop()
  lists.insert(0,root.val)
  if root.left:
    stack.append(root.left)
  if root.right:
    stack.append(root.right)
