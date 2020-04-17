class TreeNode:
  def __init__(self,x):
    self.val = x
    self.left = None
    self.right = None


lists = []
stack = [root]
while stack:
  root = stack.pop()
  lists.append(root.val)
  if root.right:
    stack.append(root.right)
  if root.left:
    stack.append(root.left)
  
