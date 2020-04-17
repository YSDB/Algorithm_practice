class ListNode:
  def __init__(self,x):
    self.val = x
    self.next = None

class Solution:
  def reversal(linkedlist):
    pre = None
    while linkedlist:
      temp = linkedlist.next
      linkedlist.next = pre
      pre = linkedlist
      linkedlist = temp
    return pre
