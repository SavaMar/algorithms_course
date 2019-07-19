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

  def reverse_list(self):
    prev = None
    current = self.head
    next_node = current.next
    
    while next_node:
      current.next = prev
      prev = current
      current = next_node
      next_node = current.next

    self.head = current
    current.next = prev
      

el1 = Element(11)
el2 = Element(22)
el3 = Element(33)
el4 = Element(44)



ll = LinkedList(el1)
ll.append(el2)
ll.append(el3)
ll.append(el4)
print(ll.get_all_nodes())
ll.reverse_list()

print(ll.get_all_nodes())