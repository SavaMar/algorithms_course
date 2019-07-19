class Element(object):
    def __init__(self,value):
      self.value = value
      self.next = None
  
class LinkedList(object):
  def __init__(self, head=None):
    self.head = head

  def append(self, new_node):
    if self.head:
      current = self.head
      while current.next != None:
        current = current.next
      current.next = new_node
    else:
      self.head = new_node
  
  def get_all_nodes(self):
    a = []
    current = self.head
    while current.next:
      a.append(current.value)
      current = current.next
    a.append(current.value)
    return a

  def middle_node(self):
    slow = fast = self.head
    fast = slow.next
    while fast and fast.next:
      slow = slow.next
      fast = slow.next.next
    return slow


el1 = Element(11)
el2 = Element(22)
el3 = Element(33)
el4 = Element(44)
el5 = Element(55)
el6 = Element(66)



ll = LinkedList(el1)
ll.append(el2)
ll.append(el3)
ll.append(el4)
ll.append(el5)
ll.append(el6)

print(ll.get_all_nodes())
print(ll.middle_node().value)