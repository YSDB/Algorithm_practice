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
    
  if root.left:
    stack.append((root.left,new))
  stack.append()
