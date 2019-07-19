'''
Write a function that searches a given key ‘x’ in a given singly linked list. 
The function should return true if x is present in linked list and false otherwise.
''''
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
    
    def is_element(self, x):
        current = self.head
        while current:
            if current.value == x:
                return True
            current = current.next
        return False