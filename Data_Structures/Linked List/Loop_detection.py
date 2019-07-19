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
  
  def del_node(self, node):
    node.value = node.next.value
    node.next = node.next.next
  
  def loop_detection(self):
        slow_p = fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next 
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                self.del_node(slow_p)
                return 1
            return 0
        

el1 = Element(11)
el2 = Element(22)
el3 = Element(33)
el4 = Element(44)
el5 = Element(55)
el6 = Element(66)
el7 = Element(77)
el8 = Element(88)
el9 = Element(99)


ll = LinkedList(el5)
ll.append(el2)
ll.append(el3)
ll.append(el4)
ll.append(el5)
ll.append(el6)
ll.append(el7)
ll.append(el8)
ll.append(el9)
ll.append(el3)
print(ll.get_all_nodes())
print(ll.loop_detection().value)
# print(ll.get_all_nodes())
# ll.del_node(el2)
# print(ll.get_all_nodes())
