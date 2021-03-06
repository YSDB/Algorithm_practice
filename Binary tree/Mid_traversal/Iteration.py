class TreeNode:
  def __init__(self,x):
    self.val = x
    self.left = None
    self.right = None

new = 0
old = 1
lists = []
stack = [(root,new)]
while stack:
  root, stat = stack.pop()
  if stat == old:
    lists.append(root.val)
    continue
  if root.right:
    stack.append((root.right,new))
  stack.append((root,old))
  if root.left:
    stack.append((root.left,new))
